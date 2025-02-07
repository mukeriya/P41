# try:
#     x = int(input('Enter x:'))
#     y = int(input('Enter y:'))
#
#     print(x / y)
# except ValueError:
#     print('Invalid input')
# except ZeroDivisionError:
#     print('We cannot divide by zero')
#
#
# print('End')
# from typing import Union
#
# try:
#     x = int(input('Enter x:'))
#     y = int(input('Enter y:'))
#
#     print(x / y)
# except (ValueError) as exception:
#     print('Invalid input', exception)
# except ZeroDivisionError as exception:
#     print(exception)
#
# print('End')

# def safe_input(cast_type, prompt):
#     while True:
#         try:
#             value = cast_type(input(prompt))
#             return value
#         except ValueError:
#             print('Invalid input')
#
#
# x = safe_input(int, 'Enter x: ')
#
# print(x)

# try:
#     x = int(input('Enter x:'))
#     y = int(input('Enter y:'))
#
#     print(x / y)
# except (ValueError) as exception:
#     print('Invalid input', exception)
# except ZeroDivisionError as exception:
#     print(exception)
# finally:
#     print('Always')


# class BuilderError(Exception):
#     pass
#
# def test():
#     # file = open('test.txt')
#     try:
#         raise BuilderError
#         # return 1 / 0
#     except BuilderError:
#         print('Builder')
#         return 2
#     finally:
#         # file.close()
#         print('End')
#
#
# print(test())


# def sum_of_list(sequence: list[int]):
#     if not isinstance(sequence, list):
#         raise ValueError('YOU CANNOT PASS SOMETHING DIFFERENT FROM LIST')
#
#     return (sum(sequence))
#
#
# print(sum_of_list([1, 2, 3]))
# print(sum_of_list('kjg'))

try:
    x = int(input('Enter x:'))
    y = int(input('Enter y:'))

    print(x / y)
except int as exception:
    print('Invalid input', exception)
except ArithmeticError:
    print('Err')
except ZeroDivisionError as exception:
    print(exception)
finally:
    print('Always')

def first_ver():
    ...


def second_ver():
    try:
        ...
    except:
        ...

try:
    first_ver()
except:
    ...