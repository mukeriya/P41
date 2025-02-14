size = int(input("enter the size of rows :"))

for i in range(0, size + 1):

    for j in range(0, size - i):
        print(end=" ")

    for j in range(0, i):
        print("*", end=" ")

    print()


for i in range(size - 1, 0, -1):

    for j in range(0, size - i):
        print(end=" ")

    for j in range(0, i):
        print("*", end=" ")

    print()
