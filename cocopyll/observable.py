from abc import ABC
from collections.abc import Iterable, Sequence
from dataclasses import dataclass

import numpy as np


class FloatObservable(ABC):
    pass


class BoolObservable(ABC):
    """
    Abstract base class for all observable of underlying type bool.
    """
    pass


@dataclass
class Not(BoolObservable):
    """
    True if observable is False and viceversa.
    """
    
    def __str__(self) -> str:
        return f'~({self.observable})'


@dataclass
class AndObs(BoolObservable):
    """
    True if and only if all observables are True.
    """

    observables: Sequence[BoolObservable]

    def __init__(self, *observables: BoolObservable) -> None:
        self.observables = tuple(observables)
        assert any(self.observables), 'At least one observable is required'
        self.observables = tuple(self._flattened_observables)

    @property
    def _flattened_observables(self) -> Iterable[BoolObservable]:
        for observable in self.observables:
            if isinstance(observable, AndObs):
                yield from observable
            else:
                yield observable

    def __str__(self) -> str:
        return ' & '.join(f'({observable})' for observable in self.observables)


@dataclass
class OrObs(BoolObservable):
    """
    True if at least on of observables is True.
    """

    observables: Sequence[BoolObservable]

    def __init__(self, *observables: BoolObservable) -> None:
        self.observables = tuple(observables)
        assert any(self.observables), 'At least one observable is required'
        self.observables = tuple(self._flattened_observables)

    @property
    def _flattened_observables(self) -> Iterable[BoolObservable]:
        for observable in self.observables:
            if isinstance(observable, OrObs):
                yield from observable
            else:
                yield observable

    def __str__(self) -> str:
        return ' | '.join(f'({observable})' for observable in self.observables)


@dataclass
class GreaterOrEqualThan(BoolObservable):
    """
    True if and only if observable1 is greater or equal than observable2.
    """

    observable1: FloatObservable
    observable2: FloatObservable
    
    def __str__(self) -> str:
        return f'({self.observable1} >= {self.observable2})'


@dataclass
class GreaterThan(BoolObservable):
    """
    True if and only if observable1 is strictly greater than observable2.
    """

    observable1: FloatObservable
    observable2: FloatObservable
    
    def __str__(self) -> str:
        return f'({self.observable1} > {self.observable2})'


@dataclass
class At(BoolObservable):
    """
    True only at date.

    >>> print(At('2023-12-29'))
    2023-12-29
    """

    date: np.datetime64
    
    def __str__(self) -> str:
        return str(self.date)


