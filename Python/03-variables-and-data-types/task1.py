digit1 = input("Enter the first digit: ")
digit2 = input("Enter the second digit: ")
digit3 = input("Enter the third digit: ")

result = int(digit1 + digit2 + digit3)

print("Result is: ", result)

#or

number = int(input("Enter a three-digit number: "))

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

result = digit1 + digit2 + digit3

print("The sum of the digits is:", result)

# or

number = input("Enter a three-digit number: ")

result = int(number[0]) + int(number[1]) + int(number[2])

print("The sum of the digits is:", result)

