def encrypt(x, y):
    if len(x) == 0:
        raise ValueError('can not encrypt empty string')
    elif y == 0:
        raise ValueError('offset must not be zero')
