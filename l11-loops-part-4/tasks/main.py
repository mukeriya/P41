from colorama import Back
BLOCK = Back.MAGENTA + "  " + Back.RESET

side_size = int(input("Enter the size of a side: "))

line = BLOCK * side_size

for _ in range(side_size):
    print(line)


