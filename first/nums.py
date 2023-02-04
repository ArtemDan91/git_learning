def plus(a: int | float, b: int | float) -> int | float:
    return a + b


def minus(a: int | float, b: int | float) -> int | float:
    return a - b

def multy(a: int | float, b: int | float) -> int | float:
    return a * b


if __name__ == '__main__':
    print(plus(2, 2))
    print(minus(10, 5))
    print(multy(2, 3))
