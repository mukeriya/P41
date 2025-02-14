# Conditional Statements

```python
print(True)  # Правда
print(False)  # Брехня

print('1 == 1', 1 == 1)  # True
print('1 == 2', 1 == 2)  # False
print('1 != 2', 1 != 2)  # True
print('1 != 1', 1 != 1)  # False
print('1 > 1', 1 > 1)  # False
print('1 < 1', 1 < 1)  # False
print('1 > 2', 1 > 2)  # False
print('2 > 1', 2 > 1)  # True
print('1 < 2', 1 < 2)  # True
print('1 >= 1', 1 >= 1)  # True
print('1 <= 1', 1 <= 1)  # True
print('1 <= 2', 1 <= 2)  # True
print('1 >= 2', 1 >= 2)  # False

# == - дорівнює
# != - не дорівнює
# > - більше
# < - менше
# >= - більше або дорівнює
# <= - менше або дорівнює
```

```python
print(True + True)  # 2
print(int(True))  # 1
print(int(False))  # 0
print(bool(156))  # True
print(bool(0))  # False
print(bool(-10))  # True
print(bool(0.0000000000000000000001))  # True
print(bool('Hello'))  # True
print(bool('False'))  # True
print(bool(' '))  # True
print(bool(''))  # False

a = 0

print(bool(a))  # False
print(bool(None))  # False

# Naming
is_admin = False
has_wifi = True
```

```python
a = True
b = True

print(a and b)  # True
print(a or b)  # True

a = True
b = False

print(a and b)  # False
print(a or b)  # True

a = False
b = True

print(a and b)  # False
print(a or b)  # True

# True and True = 1 and 1 = 1 + 1 = 2
# True and False = 1 or 1 = 1 + 0 = 1
a = False
b = False

print(a and b)  # False
print(a or b)  # False
```

```python
a = True

print(not a)  # False

a = False
print(not a)  # True

a = 5
print(not a)  # False

print(not '')  # True
```

```python
True and True  # Check two values
False and True  # Check only first

True or True  # Check only first
False or True  # Check two values

print(True and True and False)
```
## Example
```python
time = int(input('Enter current time: ')) % 24  # 26 = 2
has_ticket = True
has_money = False
has_luggage = True

# print(has_money or has_ticket and not has_luggage and time > 6)
# 2 + 2 * 2
# not - 1
# and - 2
# or  - 3

right_time = time > 6
can_use_metro = has_money or has_ticket

print(can_use_metro and not has_luggage and right_time)
```
```python
time = int(input('Enter current time: ')) % 24  # 26 = 2
user_answer = input('You have ticket? (yes/no): ')
has_ticket = user_answer == 'yes'

money_amount = int(input('Enter money amount: '))

TICKET_PRICE = 100

has_money = money_amount > TICKET_PRICE
has_luggage = True
```
## Example
```python
car_speed = 120

if 50 < car_speed < 100:
    print('chut chut (troshki) Chudovo')

print('End')
```
```python
car_speed = 50

if car_speed > 50:
    print('chut chut (troshki) Chudovo')
else:
    print('Ne chudovo (trishechki)')
```
```python
is_logged = True
is_admin = True
has_wifi = True

if has_wifi:
    if is_logged:
        if is_admin:
            print('Admin panel')
        else:
            print('Access denied')
    else:
        print('Please login')
else:
    print('No connection')

if not has_wifi:
    print('No connection')
    exit()

if not is_logged:
    print('Please login')
    exit()

if not is_admin:
    print('Access denied')
    exit()

print('Admin panel')

```