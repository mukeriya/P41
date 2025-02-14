def find(value: int, elements: list[int]) -> int:
    for index, el in enumerate(elements):
        if el == value:
            return index

    return -1
