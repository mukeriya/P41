from colorama import Back

BLOCK = Back.MAGENTA + "  " + Back.RESET

height = int(input("Enter the height: "))
width = int(input("Enter the width: "))

line = BLOCK * width

for _ in range(height):
    print(line)
