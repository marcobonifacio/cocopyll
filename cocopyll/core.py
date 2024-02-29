"""
Core module.
"""
from collections.ABC import Callable, Sequence
from datetime import date
import doctest


# Process primitives (Figure 6)
def K(a: float) -> Callable[[date], Sequence[float]]:
    """
    It is a contract that has no rights and no obligations.

    >>> zero()
    10
    """
    return K


if __name__ == '__main__':
    doctest.testmod()
