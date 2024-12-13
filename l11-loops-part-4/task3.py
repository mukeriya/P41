from colorama import Back

BLOCK = Back.LIGHTMAGENTA_EX + '  ' + Back.RESET
SPACE = '  '

size = int(input('Enter size: '))

for row in range(size):
    for column in range(size):
        if row == 0 or row == (size - 1) or column == 0 or column == (size - 1):
            print(BLOCK, end='')
        else:
            print(SPACE, end='')
    print()

print()

print(BLOCK * size)
for _ in range(size - 2):
    print(BLOCK + (SPACE * (size - 2)) + BLOCK)
print(BLOCK * size)
