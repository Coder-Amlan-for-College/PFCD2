def add(a,b):
    """
    >>> add(2,3)
    5

    >>> add(5,7)
    12

    """
    return a+b

import doctest
doctest.testmod(verbose=True)