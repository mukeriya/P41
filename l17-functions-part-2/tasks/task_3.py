def list_statistics(elements: list[int]) -> dict[str, int]:
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    for el in elements:
        if el % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if el > 0:
            positive_count += 1
        elif el < 0:
            negative_count += 1

    return {
        'even_count': even_count,
        'odd_count': odd_count,
        'positive_count': positive_count,
        'negative_count': negative_count
    }
