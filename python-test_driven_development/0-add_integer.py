#!/usr/bin/python3
''' Integer addition'''


def add_integer(a, b=98):
    """out puts an  integer addition of a and b.
    Float arguments arechanged to   integers before adding them .
    Raises:
        TypeError: If either of a or b is not an  integer or  float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
