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

10 -> bit -> bit / download_speed = amount_of_seconds_to_download / 3600
