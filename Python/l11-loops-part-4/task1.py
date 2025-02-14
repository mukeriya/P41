from colorama import Back

BLOCK = Back.LIGHTMAGENTA_EX + '  ' + Back.RESET

size = int(input('Enter size: '))

for _ in range(size):
    for _ in range(size):
        print(BLOCK, end='')
    print()

print()

for _ in range(size):
    print(BLOCK * size)
