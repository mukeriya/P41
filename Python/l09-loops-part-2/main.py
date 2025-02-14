number = None

while True:

    user_input = input('Enter number: ')
    if user_input.isdigit():
        number = int(user_input)
        break

    print('Invalid value')

print(number)
