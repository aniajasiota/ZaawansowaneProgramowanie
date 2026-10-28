def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError('n should be 0 or higher')

    if n == 0:
        return 0

    a, b = 1, 1
    for i in range(n - 1):
        b += a
        a = b - a
    return a