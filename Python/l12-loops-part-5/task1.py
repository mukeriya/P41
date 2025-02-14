number = int(input('Enter number: '))

count_of_zeros = 0

sum_of_digits = 0
count_of_digits = 0

while number != 0:
    digit = number % 10
    sum_of_digits += digit
    count_of_digits += 1
    if digit == 0:
        count_of_zeros += 1

    number //= 10

print('Sum:', sum_of_digits)
print('Count:', count_of_digits)
print('Avg:', sum_of_digits / count_of_digits)
print('Count of zeros:', count_of_zeros)
