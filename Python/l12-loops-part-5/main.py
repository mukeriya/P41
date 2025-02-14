import random

from colorama import Back

BLACK_BLOCK = Back.BLACK + ' ' + Back.RESET
WHITE_BLOCK = Back.WHITE + ' ' + Back.RESET

print(BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3,
      BLACK_BLOCK * 3, WHITE_BLOCK * 3, sep='')
print(WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3,
      BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, sep='')

print(BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3,
      BLACK_BLOCK * 3, WHITE_BLOCK * 3, sep='')
print(WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3,
      BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, sep='')
print(BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3,
      BLACK_BLOCK * 3, WHITE_BLOCK * 3, sep='')
print(WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3,
      BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, sep='')
print(BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3,
      BLACK_BLOCK * 3, WHITE_BLOCK * 3, sep='')
print(WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, WHITE_BLOCK * 3,
      BLACK_BLOCK * 3, WHITE_BLOCK * 3, BLACK_BLOCK * 3, sep='')

user_choice = 1

if user_choice == 1:
    min_value = 1
    max_value = 10
    amount_of_questions = 5
else:
    min_value = 1
    max_value = 20
    amount_of_questions = 10

x = random.randint(min_value, max_value)
y = random.randint(min_value, max_value)

print()
