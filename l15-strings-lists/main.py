# elements = ['asd', 'asd', True]
#
# for item in elements:
#     print(item.upper())
import random

# users: list[str] = ['Petro', 'Oleksiy', 'John']
#
# x: int = 5
#
# message: str = 'Hello'

# users = ['Petro']
#
# users.append('Sasha')
# users.append('Hello')
# users.pop()
# users.pop(0)
# users.remove('Sasha')
# users.index('Sasha')
# users_copy = users.copy()
# users.reverse()
# users.extend(['Hello', 'World'])
# users.insert(0, 'Petro')

# print(input('Hello'))
# admins = ('admin1', 'admin2')
# admins = 'admin1', 'admin2'
# admins = ('admin1',)
# admins = 'admin1',
#
# admins = tuple(['Hello'])

# admins = tuple(input('Enter admin names: ').split())
#
# print(admins)
#
# win_combinations = (
#     (1, 2, 3),
#     (),
#     ()
# )
#
# print(list(win_combinations))
# print(win_combinations)

# print([1, 2, 3] + [4, 5, 6])
# first_half = [1, 2, 3]
# second_half = [4, 5, 6]
# print(first_half + second_half)

# numbers = {10, 1, 2, 3, 4, 5, 5, 5}
# print(numbers)

# numbers.add(6)
# numbers.copy()
# numbers.remove(1)
# numbers.pop()
# numbers.clear()
# numbers.union()


# print(numbers)
# print(numbers.union({10, 20, 30}))
# numbers.update({10, 20, 30})
# print(numbers)

# x = {1, 2, 3, 4, 5}
# y = {4, 5, 6, 7, 8}

# print(x.intersection(y))
# print(x.difference(y))
# print(y.difference(x))
# print(x.symmetric_difference(y))

# print(x)
# x.difference_update(y)
# print(x)


# x = {1, 2, 3, 4, 5, 6, 7}
# y = {3, 4, 5}
#
# print(x.issubset(y))
# print(y.issubset(x))
# print(x.issuperset(y))

# x = {1, 2, 3}
#
# x.discard(4)
#
# print(x)


# x = {1, 2, 3}
# y = {4, 5, 6}
#
# print(x.isdisjoint(y))
#
# x = {1, 2, 3, 4}
# y = {4, 5, 6, 7}
#
# print(x.isdisjoint(y))


# x = {1, 2, 3, 4, 5}
# y = {4, 5, 6, 7, 8}
#
# print(x & y)  # intersection
# print(x - y)  # difference
# print(y - x)  # difference
# print(x ^ y)  # symmetric_difference
# print(x | y)  # union
#
# elements = [1, 2, 3, 4]
#
# for index, value in enumerate(elements):
#     if index % 3 == 0:
#         print(index, value)

random_numbers = []

for i in range(10):
    random_numbers.append(random.randint(-10, 10))

print(random_numbers)

positive_numbers = []

for i in random_numbers:
    if i > 0:
        positive_numbers.append(i)

print(positive_numbers)

even_numbers = [i * 10 for i in random_numbers if i % 2 == 0]

# return statement | loop | if condition

print(even_numbers)

random_numbers = [random.randint(-10, 10) for _ in range(10)]

print(random_numbers)

matrix = [[x, y, z] for x in range(10) for y in range(10) for z in range(10)]

print(matrix)
