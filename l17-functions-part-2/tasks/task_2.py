def find_max(elements: list[int]) -> int:
    if not elements:
        raise ValueError('list Cannot be None')
    max_num = elements[0]

    for el in elements:
        if el > max_num:
            max_num = el

    return max_num
