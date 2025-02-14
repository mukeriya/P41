# def format_title(title: str):
#     return title.capitalize().center(100, '-')
#
#
# print(format_title('Store'))
# print(format_title('account'))
# print(format_title('SETTINGS'))
#
# print()
#
# print('Store'.capitalize().center(100, '-'))
# print('account'.capitalize().center(100, '-'))
# print('SETTINGS'.capitalize().center(100, '-'))


# def get_weather_info():
#     pass

# greetings = ' Hello world'
#
#
# def show_greetings():
#     print(greetings)
#
#
# # show_greetings()
# # show_greetings()
# # show_greetings()
# # show_greetings()
#
# def convert_to_fahrenheit(celsius: float):
#     return (celsius * 9 / 5) + 32
#
#
# # print(show_greetings())
# # print(show_greetings)
#
#
# print(convert_to_fahrenheit(50))
#
#

# def show_sum(a: float, b: float):
#     print(a + b)
#
#
# show_sum(3, 8)
#
# a = 3
# b = 50
#
# show_sum(a, b)
# show_sum(10, b)


# Створіть функцію яка буде приймати 3 числа
# та виводити на екран добуток цих цисел

#
# def convert_to_fahrenheit(celsius: float):
#     return (celsius * 9 / 5) + 32
#
#
# print(convert_to_fahrenheit(50))
# f = convert_to_fahrenheit(50)
#
# print('Result: ', f * 5 / 2)
#
#
# def is_even_or_odd(number: int):
#     if number % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'
#
#
# print(is_even_or_odd(2))
# print(is_even_or_odd(3))
#
#
# def find_in_list(numbers: list[int], search_number: int):
#     for index, value in enumerate(numbers):
#         if search_number == value:
#             return index
#
#     return -1
#
#
# numbers = [1, 2, 3, 4]
#
# print(find_in_list(numbers, 1))
# print(find_in_list(numbers, 4))
# print(find_in_list(numbers, 5))
#
#
# def show_odd_numbers():
#     pass
#
#
# def number_to_list(number: int):
#     digits = []
#     while number > 0:
#         digit = number % 10
#         digits.append(digit)
#         number //= 10
#     return digits
#
#
# print(number_to_list(123456))
#
#
# def is_happy(number: int):
#     if not (100_000 <= number < 1_000_000):
#         return
#
#     digits = number_to_list(number)
#
#     # calc sum of first three elements and other three elements
#
#


def pow(number: int, e: int = 2) -> int:
    for _ in range(e - 1):
        number *= number

    return number


print(pow(12))
print(pow(12, 3))
