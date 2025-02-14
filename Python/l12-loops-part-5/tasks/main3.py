# task1
print("1. Count digits")
print("2. Calculate sum of digits")
print("3. Calculate average of digits")
print("4. Count zeros")
print("5. Exit")
choice = input("Choose an option: ")

if choice == '5':
    exit()

if choice not in ['1', '2', '3', '4']:
    print("Invalid option. Try again.")
    exit()

number = input("Enter a number: ")
if not number.isdigit():
    print("Invalid input. Please enter a positive integer.")
    exit()

digits = [int(d) for d in number]

if choice == '1':
    print("Number of digits:", len(digits))
elif choice == '2':
    print("Sum of digits:", sum(digits))
elif choice == '3':
    print("Average of digits:", sum(digits) / len(digits))
elif choice == '4':
    print("Number of zeros:", digits.count(0))

    # task2
    # n = int(input("Enter the size of a desk: "))
    #
    # for i in range(n):
    #     for j in range(n):
    #         if (i + j) % 2 == 0:
    #             print("***", end="")
    #         else:
    #             print("---", end="")
    #     print()

    # task3
    # import random
    #
    # while True:
    #     points = 0
    #     print('1. Easy')
    #     print('2. Medium')
    #     print('3. Hard')
    #
    #     user_choice = int(input('Select: '))
    #
    #     if user_choice == 1:
    #         lower_bound = 1
    #         upper_bound = 10
    #         amount_of_questions = 5
    #     elif user_choice == 2:
    #         lower_bound = 10
    #         upper_bound = 20
    #         amount_of_questions = 10
    #     elif user_choice == 3:
    #         lower_bound = 15
    #         upper_bound = 30
    #         amount_of_questions = 15
    #     else:
    #         print('Invalid choice!')
    #         continue
    #
    #     for _ in range(amount_of_questions):
    #         x = random.randint(lower_bound, upper_bound)
    #         y = random.randint(lower_bound, upper_bound)
    #         result = x * y
    #         print(str(x) + ' * ' + str(y) + ' = ', end='')
    #         user_answer = int(input())
    #
    #         if user_answer == result:
    #             points += 1
    #
    #     print('Your score: ' + str(points) + '/' + str(amount_of_questions))
    # break

#
# n = 5
#
# for i in range(n):
#     print(" " * (n - i - 1) + "■" * (2 * i + 1))
# for i in range(n - 2, -1, -1):
#     print(" " * (n - i - 1) + "■" * (2 * i + 1))
