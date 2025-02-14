from colorama import Back

BLOCK = Back.LIGHTMAGENTA_EX + '  ' + Back.RESET
SPACE = '  '

height = int(input('Enter height: '))
width = int(input('Enter width: '))

for row in range(height):
    for column in range(width):
        if row == 0 or row == (height - 1) or column == 0 or column == (width - 1):
            print(BLOCK, end='')
        else:
            print(SPACE, end='')
    print()

print()

print(BLOCK * width)
for _ in range(height - 2):
    print(BLOCK + (SPACE * (width - 2)) + BLOCK)
print(BLOCK * width)
