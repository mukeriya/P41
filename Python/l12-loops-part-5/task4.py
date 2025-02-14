# import colorama
# from colorama import init
#
# init(autoreset=True)
# size = 10
#
# BLOCK = colorama.Back.LIGHTCYAN_EX + '  '
# SPACE = '  '
#
# if size % 2 == 0:
#     size += 1
#
# for i in range(1, size, 2):
#     print(SPACE * ((size - i) // 2) + BLOCK * i)
# for i in range(size, 0, -2):
#     print(SPACE * ((size - i) // 2) + BLOCK * i)
#
# print()
#
# rows = 4
#
# for i in range(1, rows + 1):
#
#     for j in range(1, rows - i + 1):
#         print(end=" ")
#
#     for j in range(1, rows + 1):
#         print("*", end=" ")
#     print()
from colorama import Back, init

init(autoreset=True)

SIZE = 10
BLOCK = Back.LIGHTCYAN_EX + '  '
SPACE = '  '

for i in range(SIZE):
    print(SPACE * i + BLOCK * (SIZE - i))