number = int(input("Enter a four-digit number: "))  # 5646

digit1 = number // 1000  # 5646 // 1000 = 5
digit2 = (number // 100) % 10  # 5646 // 100 = 56 % 10 = 6
digit3 = (number // 10) % 10  # 5646 // 10 = 564 % 10 = 4
digit4 = number % 10  # 6

result = digit1 * digit2 * digit3 * digit4

print("The product of the digits is:", result)

# or

number = input("Enter a four-digit number: ")

digits = [int(digit) for digit in number]  # List comprehension

result = digits[0] * digits[1] * digits[2] * digits[3]

print("The product of the digits is:", result)
