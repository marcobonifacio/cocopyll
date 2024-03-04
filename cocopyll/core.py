from datetime import date
from decimal import Decimal
import doctest
from enum import StrEnum
from typing import NamedTuple


class Currency(Enum):
    """
    Enumerations of currencies.

    >>> print(Currency.USD)
    USD
    """

    USD = 'USD'
    EUR = 'EUR'
    JPY = 'JPY'
    GBP = 'GBP'
    CAD = 'CAD'
    AUD = 'AUD'

    def __str__(self) -> str:
        return f'{self.value}'


class Cashflow(NamedTuple):
    """
    Structure for cashflow.

    >>> print(Cashflow(Decimal('13'), Currency.EUR, date(2024, 1 , 16)))
    Cashflow(amount=Decimal('13.0'), currency=Currency.EUR, date=date(2024, 1,
    16))
    """
    amount: Decimal
    currency: Currency
    date: date

    def __init__(
        self, amount: str | float, currency: str, date: str
    ) -> None:
        self.amount = Decimal(amount)
        currency = 
        date = 


if __name__ == '__main__':
    doctest.testmod()
