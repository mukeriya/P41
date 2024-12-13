from colorama import Back

BLACK_BLOCK = Back.BLACK + " " + Back.RESET
WHITE_BLOCK = Back.WHITE + " " + Back.RESET
cell_size = int(input("Enter cell size: "))

BOARD_SIZE = 8

for _ in range(BOARD_SIZE // 2):
    print((BLACK_BLOCK * cell_size + WHITE_BLOCK * cell_size) * 4)
    print((WHITE_BLOCK * cell_size + BLACK_BLOCK * cell_size) * 4)
