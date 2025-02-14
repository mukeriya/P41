from colorama import Back, init

init(autoreset=True)

ROWS = 8
COLUMNS = 8

BLACK_BLOCK = Back.BLACK + ' '
WHITE_BLOCK = Back.WHITE + ' '

block_size = int(input('Enter block size: '))

black_extended_block = BLACK_BLOCK * block_size
white_extended_block = WHITE_BLOCK * block_size

for row in range(ROWS):
    for column in range(COLUMNS):
        if (row + column) % 2 == 0:
            print(black_extended_block, end='')
        else:
            print(white_extended_block, end='')
    print()

print()

for row in range(ROWS):
    for column in range(COLUMNS):
        block = black_extended_block if (row + column) % 2 == 0 else white_extended_block
        print(block, end='')
    print()
