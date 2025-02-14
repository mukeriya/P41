# import os
# import time
#
# n = 6
# GREEN = '\033[0;32m'
# END = '\033[0m'
# board = [[-1 for _ in range(n)] for _ in range(n)]
#
# moves_x = [2, 1, -1, 2, -2, -1, 1, 2]
# moves_y = [1, 2, 2, 1, -1, -2, -2, -1]
#
#
# def is_safe(x, y, board):
#     return 0 <= x < n and 0 <= y < n and board[x][y] == -1
#
#
# def print_board(move_count):
#     os.system('cls')
#     for row in board:
#         print(' '.join((f'{cell:2}' if cell != move_count else f'{GREEN}{cell:2}{END}') if cell != -1 else '. ' for cell in row))
#
#     time.sleep(0.1)
#
#
# def solve_knight_tour(x, y, move_count, board):
#     if move_count == n * n:
#         return True
#
#     for i in range(8):
#         new_x = x + moves_x[i]
#         new_y = y + moves_y[i]
#
#         if is_safe(new_x, new_y, board):
#             board[new_x][new_y] = move_count
#             print_board(move_count)
#
#             if solve_knight_tour(new_x, new_y, move_count + 1, board):
#                 return True
#
#             board[new_x][new_y] = -1
#
#     return False
#
#
# def knight_tour(start_x, start_y):
#     board[start_x][start_y] = 0
#
#     if solve_knight_tour(start_x, start_y, 1, board):
#         print('Tour Completed!')
#     else:
#         print('Solution does not exists')
#
#
# start_x = 0
# start_y = 0
#
# knight_tour(start_x, start_y)
import os.path

# file = open('./test.txt', 'w')
#
# file.write('Hello students!')
#
# file.close()
# file = open('./test.txt', 'w')


# print(file.read())
# w(+/b) - Write
# r(+/b) - Read
# a(+/b) - Append
# file = open('./test.txt', 'a')

# file.write('\nHello again!')

# print(file.read())

# file.close()

# user_file_path = input('Enter: ')
#
# try:
#     file = open(user_file_path)
#     print(file.read())
# except FileNotFoundError:
#     print('File not found')

# print(os.path.join('home', 'user', 'dev', 'bin'))
#
# print(os.path.normpath('/home/user/bin'))

# file = open('test.txt')

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readlines())

# for line in file:
#     print(line)

# try:
#     file = open('test.txt')
#
#     print(file.read())
# finally:
#     file.close()

with open('test.txt') as file:
    with open('main.py', 'r') as main_file:
        print(file.read())
        print(main_file.read())

