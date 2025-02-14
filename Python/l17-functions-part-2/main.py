# def sum(*args):
#     print(args)
#     print(type(args))
#     total_sum = 0
#     for i in args:
#         total_sum += i
#
#     return total_sum
#
#
# print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9))
#
# nums = [1, 2, 3, 4]
#
# print(sum(*nums))
#
# print(nums)
# print(1, 2, 3, 4)
# print(*nums)
# def some_func(x, y, z, *args):
#
#
from typing import Callable


# def some_func(x, y, z, *args):
#     print(f'{x = }')
#     print(f'{y = }')
#     print(f'{z = }')
#     print(f'{args = }')
#
#
# some_func(1, 2, 3, 4, 5, 5, 6, 7, 8)

# def insert(value, sequence: list = []):
#     sequence.append(value)
#
#     return sequence
#
#
# seq_1 = insert(1)
#
# seq_1.append(3)
#
# seq_2 = insert(2)
#
# print(seq_1)
# print(seq_2)
#
# print(seq_1 == seq_2)
# print(seq_1 is seq_2)
# print(id(seq_1))
# print(id(seq_2))

# def area(width, height, something, blob):
#     pass
#
#
# area(1, 3, 34, 4)


# def pow(base, e=2):
#     return base ** e
#
#
# print(pow(5))
# print(pow(5, e=3))
#
#
# def test(a, b, c, d):
#     print(f'{a = }')
#     print(f'{b = }')
#     print(f'{c = }')
#     print(f'{d = }')


# print(test(1, 2, 3, 4))
# print(test(1, c=2, b=3, d=4))
# print(test(1, c=2, b=3, 4))

# print(1, 2, 3, sep='asd')
# print(1, 2, 3, 'asd', end='')


# def calculate_bmi(height, weight, age):
#     result = weight / (height ** 2)
#     print(f'Result for {age} is {result}')
#
#     return result


# print(calculate_bmi(height=1.8, weight=70, age=20))


# def func(x, y, *, z=1, r=2, t=3):
#     pass


# print(func(1, 2, 3, 4, 5))
# print(func(1, 2, r=3, z=4, t=5))
# print(func(1, 2))
# print(func(1, 2, r=10))

# def t(s, d, a, b):
#     return a / a
#
#
# nums = [1, 2]
#
# print(t(1, 2, *nums))

# def print_kwargs(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
#
# print_kwargs(x=1, y=2, z=3)
#
# values = {'x': 4, 'y': 5, 'z': 6}
#
# print_kwargs(values=values)
# print_kwargs(**values)
#
#
# def func(x, y, *args, **kwargs):
#     print(f'{x = }')
#     print(f'{y = }')
#     print(f'{args = }')
#     print(f'{kwargs = }')
#
# func(1, 2, 3, 4, 5, 6, u=1)
#
#
# def func(x, y, **kwargs):
#     print(x, y, kwargs)
#
#
# func(q=1, w=2, x=3, y=4)

# def func():
#     x = 1
#
#
#
# if True:
#     x = 5
#
#
# print(x)

# x = 5
#
#
# def first():
#     global x
#     print(x)
#     x = 10
#     print(x)


# LEGB
# Local
# Enclosed
# Global
# Built-in

# first()
# print(x)

# x = 5
#
# def calculate():
#     global x
#
#     x += 10


# x = 5
#
#
# def first():
#     x = 10
#
#     def second():
#         x = 15
#
#         def third():
#             nonlocal x
#             x = 20
#             print(x)
#
#         third()
#         print(x)
#
#     second()
#     print(x)


# first()
# print(x)


# def say_hello():
#     print('Hello')
#
#
# greetings = say_hello
#
# greetings()

# def filter(elements: list[int], predicate: Callable[[int], bool]):
#     result = []
#
#     for i in elements:
#         if predicate(i):
#             result.append(i)
#
#     return result
#
#
# def is_even(x: int):
#     return x % 2 == 0
#
#
# def is_odd(x: int):
#     return x % 2 != 0
#
#
# def is_prime(x: int):
#     pass


# nums = [1, 2, 3, 4, 5, 6, 76, 100]
#
# even_numbers = filter(nums, is_even)
#
# print(even_numbers)
#
# odd_numbers = filter(nums, is_odd)
#
# print(odd_numbers)


# def greetings(text: str, on_finish: Callable):
#     print(text)
#     on_finish()
#
#
# def finish_print():
#     print('End')
#
#
# greetings('Hello', finish_print)
#
# from tkinter import Tk, Button
#
# tk = Tk()
#
#
# def on_button_click():
#     print('Button click')
#
#
# button = Button(tk, text='Click me', command=on_button_click)
#
# button.place(x=100, y=20)
#
# tk.mainloop()

# def calculate(x, y):
#     def show_results():
#         print(x + y)
#
#     return show_results
#
#
# calculate(2, 8)()


def on_delete():
    print('Delete')


def on_update():
    print('Update')


commands = {
    'on_delete': on_delete,
    'on_update': on_update
}

choice = input('Select: ')

commands[choice]()

# if choice == 'delete':
#     commands['on_delete']()
# elif choice == 'update':
#     commands['on_update']()
