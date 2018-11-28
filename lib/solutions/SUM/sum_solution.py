# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if type(x) not in [int] or type(y) not in [int]:
        raise TypeError("The arguments must be integer")
    if (x < 0) or (x > 100) or (y < 0) or (y > 100):
        raise valueError("The arguments must be in range 0-100")
    return x+y
