from abc import ABC, abstractmethod
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
import doctest
from typing import Union

from observable import BoolObservable, FloatObservable, Konst


class Contract(ABC):
    
    @abstractmethod
    def resolve(self) -> 'BaseContract':
        pass

    def __str__(self) -> str:
        return str(self.resolve())


class BaseContract(Contract):
    """
    Abstract base class for all contracts. 
    """

    def resolve(self) -> 'BaseContract':
        return self

    def __add__(self, other: 'BaseContract') -> 'BaseContract':
        return And(self, other)

    def __neg__(self) -> 'BaseContract':
        return Give(self)

    def __sub__(self, other: 'BaseContract') -> 'BaseContract':
        return And(self, Give(other))

    def __mul__(
        self, observable: Union[FloatObservable, float]
    ) -> 'BaseContract':
        if isinstance(observable, FloatObservable):
            return Scale(observable, self)
        elif isinstance(observable, float):
            return Scale(Konst(observable), self)
        else:
            return NotImplemented


@dataclass
class Zero(BaseContract):
    """
    Neither receive nor pay anything.

    >>> print(Zero())
    Zero
    """

    def __str__(self) -> str:
        return 'Zero'


@dataclass
class One(BaseContract):
    """
    Receive one unit of currency at acquisition. 
    
    >>> print(One('EUR'))
    One(EUR)
    """
    
    currency: str

    def __str__(self) -> str:
        return f'One({self.currency})'


@dataclass
class Give(BaseContract):
    """
    Receive all obligations of the underlying contract and pay all rights,
    i.e. invert the underlying contract.

    >>> print(Give(One('EUR')))
    Give(One(EUR))
    """

    contract: BaseContract

    def __str__(self) -> str:
        return f'Give({self.contract})'


@dataclass
class And(BaseContract):
    """
    Obtain rights and obligations of all underlying contracts.
    >>> print(And(One('EUR'), Give(One('USD'))))
    And(One(EUR), Give(One(USD)))
    """

    contracts: Sequence[BaseContract]

    def __init__(self, *contracts: BaseContract) -> None:
        self.contracts = tuple(contracts)
        assert any(self.contracts), 'At least one contract is required'
        self.contracts = tuple(self._flattened_contracts)

    @property
    def _flattened_contracts(self) -> Iterable[BaseContract]:
        for contract in self.contracts:
            if isinstance(contract, And):
                yield from contract.contracts
            else:
                yield contract

    def __str__(self) -> str:
        contracts = tuple(str(contract) for contract in self.contracts)
        return f'And({", ".join(contracts)})'


@dataclass
class Or(BaseContract):
    """
    Choose at acquisition between the underlying contracts.

    >>> print(Or(One('EUR'), One('USD')))
    Or(One(EUR), One(USD))
    """
    
    contracts: Sequence[BaseContract]

    def __init__(self, *contracts: BaseContract) -> None:
        self.contracts = tuple(contracts)
        assert any(self.contracts), 'At least one contract is required'
        self.contracts = tuple(self._flattened_contracts)

    @property
    def _flattened_contracts(self) -> Iterable[BaseContract]:
        for contract in self.contracts:
            if isinstance(contract, Or):
                yield from contract.contracts
            else:
                yield contract

    def __str__(self) -> str:
        contracts = tuple(str(contract) for contract in self.contracts)
        return f'Or({", ".join(contracts)})'


@dataclass
class Cond(BaseContract):
    """
    If observable is True at acquisition, obtain contract1, 
    otherwise contract2.
    """

    observable: BoolObservable
    contract1: BaseContract
    contract2: BaseContract

    def __str__(self) -> str:
        return f'({self.observable}, {self.contract1}, {self.contract2})'


@dataclass
class Scale(BaseContract):
    """
    Same as the underlying contract, but all payments scaled by the value of 
    observable at acquisition.
    """

    observable: FloatObservable
    contract: BaseContract

    def __str__(self) -> str:
        return f'Scale({self.observable}, {self.contract})'


@dataclass
class When(BaseContract):
    """
    Obtain the underlying contract as soon as observable becomes True after
    acqusition.
    """

    observable: BoolObservable
    contract: BaseContract

    def __str__(self) -> str:
        return f'When({self.observable}, {self.contract})'


@dataclass
class Delay(BaseContract):
    """
    Obtain the underlying contract and delay all payments to first occurrence 
    of observable.
    """

    observable: BoolObservable
    contract: BaseContract

    def __str__(self) -> str:
        return f'Delay({self.observable}, {self.contract})'


@dataclass
class Anytime(BaseContract):
    """
    At any point in time after acquisition when observable is True, choose
    either to obtain the underlying contract or not; can be exercised only
    once.
    """

    observable: BoolObservable
    contract: BaseContract

    def __str__(self) -> str:
        return f'Anytime({self.observable}, {self.contract})'


@dataclass
class Until(BaseContract):
    """
    Obtain the underlying contract, but as soon as observable becomes True 
    after acquisition all following payments are nullified.
    """

    observable: BoolObservable
    contract: BaseContract

    def __str__(self) -> str:
        return f'Until({self.observable}, {self.contract})'


@dataclass
class Exchange(BaseContract):
    """
    Exchange cashflows resulting from contract to currency at the current 
    spot rate.

    >>> print(Exchange('USD', One('EUR')))
    Exchange(USD, One(EUR))
    """

    currency: str
    contract: BaseContract

    def __str__(self) -> str:
        return f'Exchange({self.currency}, {self.contract})'


if __name__ == '__main__':
    doctest.testmod()
