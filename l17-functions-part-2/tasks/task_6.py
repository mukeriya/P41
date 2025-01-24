def factorial(x: int) -> int:
    result = 1
    for i in range(2, x + 1):
        result *= i

    return result


def map_to_factorial(elements: list[int]) -> list[int]:
    return [factorial(el) for el in elements]
