from colorama import Back

BLOCK = Back.LIGHTMAGENTA_EX + '  ' + Back.RESET

height = int(input('Enter height: '))
width = int(input('Enter width: '))

for _ in range(height):
    for _ in range(width):
        print(BLOCK, end='')
    print()

print()

for _ in range(height):
    print(BLOCK * width)