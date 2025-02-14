METERS_TO_MILES = 0.00053995709503245226547
METERS_TO_INCHES = 39.3701
METERS_TO_YARDS = 1.093613888889

meters_amount = float(input('Enter meters amount: '))
print('1. To Miles')
print('2. To Inches')
print('3. To Yards')

user_choice = input('Select: ')

if user_choice == '5':
    print('Invalid choice')
    exit()

if user_choice == '1':
    print(meters_amount * METERS_TO_MILES)
elif user_choice == '2':
    print(meters_amount * METERS_TO_INCHES)
elif user_choice == '3':
    print(meters_amount * METERS_TO_YARDS)
else:
    print('Invalid choice')

time = int(input("Enter your time: "))

if time >= 24 or time < 0:
    print('Invalid time')
elif time < 6:
    print("Good night!")
elif time < 13:
    print("Good morning!")
elif time < 17:
    print("Good day!")
else:
    print("Good evening!")