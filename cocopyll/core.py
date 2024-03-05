"""
Core implementation of composing contracts.
"""

from datetime import date
from decimal import Decimal
import doctest
from enum import StrEnum
from typing import NamedTuple


class Currency(StrEnum):
    """
    Enumeration of currencies.

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


class Contract(StrEnum):
    """
    Enumeration of contracts.

    >>> print(Contract.ZERO)
    Zero
    """
    ZERO = 'Zero'
    ONE = 'One'
    GIVE = 'Give'
    AND = 'And'
    OR = 'Or'
    COND = 'Cond'
    SCALE = 'Scale'
    WHEN = 'When'
    ANYTIME = 'Anytime'
    UNTIL = 'Until'

    def __str__(self) -> str:
        return f'{self.value}'


class Cashflow(NamedTuple):
    """
    Structure for cashflow.

    >>> print(Cashflow(Decimal('13'), Currency.EUR, date(2024, 1 , 16)))
    Cashflow(amount=13.00, currency=EUR, date=2024-01-16)
    """
    amount: Decimal
    currency: Currency
    date: date

    def __str__(self) -> str:
        return 'Cashflow(amount={0:.2f}, currency={1}, date={2})'.format(
            float(self.amount), str(self.currency), self.date.isoformat()
        )


def parser(arg: str):
    """
    Parser for financial contracts.

    >>> parser = parser('And(One(EUR), Give(Zero))')
    >>> next(parser)
    ('And', 'One(EUR), Give(Zero)')
    >>> next(parser)
    ('One', 'EUR')
    """
    contract, argument = arg.split('(', 1)
    yield contract, argument[:-1]
    if argument[:-1].find('(') >= 0:
        parser(argument[:-1])


if __name__ == '__main__':
    doctest.testmod()
