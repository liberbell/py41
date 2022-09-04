from pydoc import doc


class Cal(object):
    """Add and double
    >>> c = Cal()
    >>> c.add_num_and_double(1, 1)
    4

    >>> c.add_num_and_double("1", "1")
    4
    """

    def add_num_and_double(self, x, y):
        result = x + y
        result *= 2
        return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()