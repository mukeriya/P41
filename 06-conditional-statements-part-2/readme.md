```python
choice = input('Enter: ')

# Best variant - 1
# Worst - 2

if choice == '1':
    print('Sum')
elif choice == '2':
    print('Avg')
else:
    print('Invalid choice')

print('End')
#
choice = input('Enter: ')

# Best - 3
# Worst - 3

if choice == '1':
    print('Sum')
if choice == '2':
    print('Avg')
if choice != '1' and choice != '2':
    print('Invalid choice')

age = int(input('Enter age: '))
height = int(input('Enter height: '))

if age > 18:
    print('Access allowed')
elif height < 120:
    print('Ne mozhesh pitu na horgu')
```

```python
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
```