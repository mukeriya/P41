height = int(input("Enter the height: "))
width = int(input("Enter the width: "))

for i in range(height):
    if i == 0 or i == height - 1:
        print("*" * width)
    else:
        print('*' + " " * (width - 2) + '*')
