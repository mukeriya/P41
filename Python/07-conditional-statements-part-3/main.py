# number = input('')
#
# if len(number) != 6:
#     print('Invalid number')
#     exit()

# number = int(input(''))
#
# if number < 100_000 or number > 999_999:
#     print('Invalid number')
#     exit()
#
# digit_1 = number // 100_000
# digit_2 = number // 10_000 % 10
# digit_3 = number // 1_000 % 10
# digit_4 = number // 100 % 10
# digit_5 = number // 10 % 10
# digit_6 = number % 10
#
# print(digit_1)
# print(digit_2)
# print(digit_3)
# print(digit_4)
# print(digit_5)
# print(digit_6)

number = 2

match number:
    case 1:
        print('Hello')
    case 3:
        print('Not hello')
    case _:
        print('Default')

letter = 'a'

match letter:
    case 'a':
        print('A')
    case 'b':
        print('B')

# weekday_number = int(input('Enter: '))
#
# match weekday_number:
#     case 1:
#         print('Monday')
#     case 2:
#         print('Tuesday')
#     case 3:
#         print('Day')
#     case 4:
#         print('Day')
#     case 5:
#         print('Day')
#     case 6:
#         print('Day')
#     case 7:
#         print('Day')
#     case _:
#         print('Invalid day')


month_number = 2

match month_number:
    case 1 | 2 | 12:
        print('Winter')
    case 3 | 4 | 5:
        print('')