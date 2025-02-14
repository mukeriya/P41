side_size = int(input("Enter the size of a side: "))

for row in range(side_size):
    if row == 0 or row == side_size - 1:
        print('*' * side_size)
    else:
        print('*' + " " * (side_size - 2) + '*')
