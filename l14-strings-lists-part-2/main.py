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
#
# for row in board:
#     for col in row:
#         print(col, end=' ')
#
#     print()
#
#
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
digits = [1, 2, 3]

digits_2 = digits.copy()
digits_2.append(4)
print(digits_2)
print(digits)
#
# print(id(digits))
# print(id(digits_2))
#

# text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sit amet dictum enim. Nam aliquet eget risus quis pharetra. Phasellus porta leo quis iaculis tempus. Proin libero odio, tempor ut orci et, laoreet semper sem. In vitae odio tincidunt, blandit nisl vel, egestas purus. Vestibulum feugiat arcu dolor, egestas scelerisque justo scelerisque dictum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam dolor orci, tempor nec porta eu, tincidunt congue dolor. Integer in dolor ante. Aenean fermentum, turpis non cursus viverra, nisi risus finibus tortor, sed placerat augue ipsum non purus. Integer felis leo, scelerisque vel risus pharetra, pretium volutpat magna. Pellentesque eu felis est. Donec pellentesque mauris eu elit molestie rutrum.'.lower()
#
# sentences = text.split('. ')
#
# # for sentence in sentences:
# #     print(sentence.upper())
#
# # for i in range(len(sentences)):
# #     print(sentences[i])
#
# for index, sentence in enumerate(sentences):
#     sentences[index] = sentence[:10]
#
# print(text)
# print('. '.join(sentences))
#
# length = 5
#
# my_list = []
#
# for _ in range(length):
#     my_list.append(input('Enter: '))
#


