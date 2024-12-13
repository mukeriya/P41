number = int(input("Enter your number: "))  
digits = 0
total = 0
zero_count = 0

temp = number

while temp > 0:
    digit = temp % 10  
    if digit == 0:
        zero_count += 1  
    total += digit       
    digits += 1          
    temp //= 10          

average = total / digits  

while True:
    print("\nMenu:")
    print("1. Count the number of digits")
    print("2. Calculate the sum of digits")
    print("3. Calculate the average of digits")
    print("4. Count the number of zeros")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print(f"Number of digits: {digits}")
    elif choice == "2":
        print(f"Sum of digits: {total}")
    elif choice == "3":
        print(f"Average of digits: {round(average, 2)}")
    elif choice == "4":
        print(f"Number of zeros: {zero_count}")
    elif choice == "5":
        print("Program terminated.")
        break
    else:
        print("Invalid choice, please try again.")
