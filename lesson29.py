def outer(a, b):

    def plus(c, d):
        return c + d
    
    r = plus(a + b)
    return r

outer(1, 2)
