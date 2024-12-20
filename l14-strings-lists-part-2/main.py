# login = 'Dako'
#
# print('Welcome', login, '. Lets start')
#
# message = 'Welcome ' + login + '. Lets start'
#
# print(message)
#
# message = 'Welcome {}. Lets start'.format(login)
#
# print(message)
import random
# message = 'Welcome {1}. {0} {0} Lets start'.format(login, 15)
#
# print(message)


# message = 'Welcome {name}. {age} {age} Lets start'.format(name=login, age=15)
#
# print(message)

# print('Your salary is {0:3.2f}'.format(531.53146))

# age = 2345
#
# print(f'Welcome {age:b}')
# print(f'Welcome {age:c}')
# print(f'Welcome {age:d}')
# print(f'Welcome {age:o}')
# print(f'Welcome {age:x}')
#
# num_1 = 10
# num_2 = -10
#
# print(f'{num_1:-}  {num_2:-}')
# print(f'{num_1:+}  {num_2:+}')
# print(f'{num_1: }|{num_2: }')
# print(f'{num_2: }|{num_2: }')
#
# points = 10
#
# name = 'Sasha'
#
# print(f'You have {points} points.')
# print(f'You have {points:10} points.')
# print(f'You have {name:10} points.')
# print(f'You have {points:>10} points.')
# print(f'You have {points:<10} points.')
# print(f'You have {points - 5:^10} points.')
# print(f'You have {points:=^10} points.')
# print(f'You have {points:=^1} points.')
#
# percent = 0.524254534

# print(f'{percent:.23%}')


# symbol = '='
# align = '^'
# width = 50
# greetings = 'Hello'

# print(f'{greetings:{symbol}{align}{width}}')


import string

#
# print(string.punctuation)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.whitespace)
# print(string.printable)

# symbols = string.punctuation + string.ascii_letters + string.digits

# print(''.join([random.choice(symbols) for _ in range(10)]))

#
# message = 'Hello world!'
#
# if 'e' in message:
#     print('Yes')
#
# if 'llo wo' in message:
#     print('Yes')
#
# if 'asda' in message:
#     print('Yes')
#
# text = input('Enter: ')
#
# L = 0
# R = len(text) - 1
# is_palindrome = True
#
# while L < R:
#     if text[L].lower() == text[L].upper():
#         L += 1
#         continue
#
#     if text[R].lower() == text[R].upper():
#         R -= 1
#         continue
#
#     if text[L].lower() != text[R].lower():
#         is_palindrome = False
#         break


# my_list = [1, 2, 3, 4, 5, 6, 7, 'Strings', True, 12.5]
#
# for elem in my_list:
#     print(elem)
#
# print(my_list[0])
# print(my_list[-1])
# print(my_list[::-1])
# print(my_list[::2])

# users = ['Sasha', 'Petro', 'Oleg', 'Pasha', 'Masha', 'Alm']
#
# for user in users:
#     print(user)
#
# print(''.center(50, '='))
#
# for user in users:
#     if 'a' in user.lower():
#         print(user)


# users = [1, 2, 3]
# digits = list([1, 2, 3])
#
# print(users)
# print(digits)
#
# empty_list = []
# empty_list = list()
#
# print(empty_list)
#
# board = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
#
# print(board[1][1])
# print(board[2][2])
# print(board[1][2])

# for row in board:
#     for col in row:
#         print(col, end=' ')
#
#     print()


# nested_list = [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
#
# print(nested_list[0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0])

# text = 'Hello world!'
#
# characters = list(text)
#
# print(characters)


# digits = [1, 345, 15, 856, 234]
#
# print(digits)
#
# digits.append(10)
#
# print(digits)
#
# digits.insert(0, 90)
#
# print(digits)
#
# digits.clear()
#
# print(digits)
#
# other_digits = [1, 2, 4]
#
# digits.extend(other_digits)
#
# print(digits)
#
# digits.reverse()
#
# print(digits)
#
# digits = [1, 1, 2, 3, 4, 4, 5, 6, 7]
#
# digits.remove(4)
#
# print(digits)
#
# print(digits.pop(0))
#
# digits[0] = 100
# print(digits)
#
# if 100 in digits:
#     print('Yes')

#
# digits = [1, 2, 3]
#
# digits_2 = digits.copy()
# digits_2.append(4)
# print(digits_2)
# print(digits)
#
# print(id(digits))
# print(id(digits_2))
#

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sit amet dictum enim. Nam aliquet eget risus quis pharetra. Phasellus porta leo quis iaculis tempus. Proin libero odio, tempor ut orci et, laoreet semper sem. In vitae odio tincidunt, blandit nisl vel, egestas purus. Vestibulum feugiat arcu dolor, egestas scelerisque justo scelerisque dictum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam dolor orci, tempor nec porta eu, tincidunt congue dolor. Integer in dolor ante. Aenean fermentum, turpis non cursus viverra, nisi risus finibus tortor, sed placerat augue ipsum non purus. Integer felis leo, scelerisque vel risus pharetra, pretium volutpat magna. Pellentesque eu felis est. Donec pellentesque mauris eu elit molestie rutrum.'.lower()

sentences = text.split('. ')

# for sentence in sentences:
#     print(sentence.upper())

# for i in range(len(sentences)):
#     print(sentences[i])

for index, sentence in enumerate(sentences):
    sentences[index] = sentence[:10]

print(text)
print('. '.join(sentences))

length = 5

my_list = []

for _ in range(length):
    my_list.append(input('Enter: '))


