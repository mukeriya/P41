# Strings

## Formatting

```python
login = 'Dako'

print('Welcome', login, '. Lets start')

message = 'Welcome ' + login + '. Lets start'

print(message)

message = 'Welcome {}. Lets start'.format(login)

print(message)
```

Result:

```commandline
Welcome Dako . Lets start
Welcome Dako. Lets start
Welcome Dako. Lets start
```

Using indexes in formatting

```python
login = 'Dako'
message = 'Welcome {1}. {0} {0} Lets start'.format(login, 15)

print(message)
```

Result:

```commandline
Welcome 15. Dako Dako Lets start
```

Using names in formatting

```python
login = 'Dako'

message = 'Welcome {name}. {age} {age} Lets start'.format(name=login, age=15)

print(message)
```

Result:

```commandline
Welcome Dako. 15 15 Lets start
```

Format floating number
> ```.2f``` means that only 2 digits after comma will be displayed
>
> ```3``` means length of string

```python
print('Your salary is {0:3.2f}'.format(531.53146))
```

Result:

```commandline
Your salary is 531.53
```

| Specification | Description    |
|:-------------:|----------------|
|   ```:b```    | Binary format  |
|   ```:c```    | Unicode symbol |
|   ```:d```    | Tens format    |
|   ```:o```    | Octal format   |
|   ```:x```    | Hex format     |

```python
age = 2345

print(f'Welcome {age:b}')
print(f'Welcome {age:c}')
print(f'Welcome {age:d}')
print(f'Welcome {age:o}')
print(f'Welcome {age:x}')
```

Result:

```commandline
Welcome 100100101001
Welcome ऩ
Welcome 2345
Welcome 4451
Welcome 929
```

---

Format negative/positive numbers

| Formatting type | Description                                      |
|:---------------:|--------------------------------------------------|
|    ```:-```     | Shows ```-``` only for negative numbers          |
|    ```:+```     | Shows ```+``` only for positive numbers          |
| ```:<space>```  | Inserts additional space before positive numbers |

```python
num_1 = 10
num_2 = -10

print(f'{num_1:-}  {num_2:-}')
print(f'{num_1:+}  {num_2:+}')
print(f'{num_1: }|{num_2: }')
print(f'{num_2: }|{num_2: }')
```

```commandline
10  -10
+10  -10
 10|-10
-10|-10
```

---

Align content

| Formatting type | Description |
|:---------------:|-------------|
|    ```:<```     | Left align  |
|    ```:>```     | Right align |
|    ```:^```     | Center      |

```python
points = 10

name = 'Sasha'

print(f'You have {points} points.')
print(f'You have {points:10} points.')
print(f'You have {name:10} points.')
print(f'You have {points:>10} points.')
print(f'You have {points:<10} points.')
print(f'You have {points - 5:^10} points.')
print(f'You have {points:=^10} points.')  # = is fill chat
print(f'You have {points:=^1} points.')
```

```commandline
You have 10 points.
You have         10 points.
You have Sasha      points.
You have         10 points.
You have 10         points.
You have     5      points.
You have ====10==== points.
```

---

Percentage formatting

```python
percent = 0.524254534

print(f'{percent:.2%}')
```

```commandline
52.43%
```

---

```python
symbol = '='
align = '^'
width = 50
greetings = 'Hello'

print(f'{greetings:{symbol}{align}{width}}')
```

```commandline
======================Hello=======================
```

---

## String module

```python
import string
import random

print(string.punctuation)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.whitespace)
print(string.printable)

symbols = string.punctuation + string.ascii_letters + string.digits

print(''.join([random.choice(symbols) for _ in range(10)]))
```

```commandline
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
0123456789abcdefABCDEF
01234567
 	

0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 	

m>2[J%jMU-
```

## Check substring/includes

```python
message = 'Hello world!'

if 'e' in message:
    print('Yes')

if 'llo wo' in message:
    print('Yes')

if 'asda' in message:
    print('Yes')
```

```commandline
Yes
Yes
```

# Lists

## Initialize list

List in python can include different type of values

### Empty list

```python
empty_list = []
empty_list = list()
```

### With values

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 'Strings', True, 12.5]

for elem in my_list:
    print(elem)
```

```commandline
1
2
3
4
5
6
7
Strings
True
12.5
```

## Indexes in list

Works same as indexes in strings (and slices)

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 'Strings', True, 12.5]

print(my_list[0])
print(my_list[-1])
print(my_list[::-1])
print(my_list[::2])
```

```commandline
1
12.5
[12.5, True, 'Strings', 7, 6, 5, 4, 3, 2, 1]
[1, 3, 5, 7, True]
```

## Multidimensional list

```python
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(board[1][1])
print(board[2][2])
print(board[1][2])

for row in board:
    for col in row:
        print(col, end=' ')

    print()
```

```commandline
5
9
6
1 2 3 
4 5 6 
7 8 9 
```

## Nested list

Lists can include other lists

```python
nested_list = [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

print(nested_list[0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0])
```

```commandline
[]
```

## Convert string into list of characters

```python
text = 'Hello world!'

characters = list(text)

print(characters)
```

```commandline
['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']
```

## Add value into list (in the end)

> ```.append``` takes only 1 argument - ```__value```.

```python
digits = [1, 345, 15, 856, 234]

print(digits)

digits.append(10)

print(digits)
```

```commandline
[1, 345, 15, 856, 234]
[1, 345, 15, 856, 234, 10]
```

## Add value into list in some position

> ```.insert``` takes 2 arguments ```__index``` and ```__object```
>
> ```__index``` - position
>
> ```__object``` - value

```python
digits.insert(0, 90)

print(digits)
```

```commandline
[90, 1, 345, 15, 856, 234, 10]
```

## Clear list

```python
digits.clear()

print(digits)
```

```commandline
[]
```

## Extend list

> ```.extend``` takes 1 argument - ```__iterable```
>
> ```__iterable``` - any iterable object (list, set)

```python
other_digits = [1, 2, 4]

digits.extend(other_digits)

print(digits)
```

```commandline
[1, 2, 4]
```

## Reverse list

```python
digits.reverse()

print(digits)
```

```commandline
[4, 2, 1]
```

## Remove value from list
- ```remove``` - removes element by value. Returns None
- ```pop``` - removes element by index. Returns removed element

```python
digits = [1, 1, 2, 3, 4, 4, 5, 6, 7]

digits.remove(4)

print(digits)

print(digits.pop(0))
```

```commandline
[1, 1, 2, 3, 4, 5, 6, 7]
1
```

## Update value in list

```python
digits[0] = 100
print(digits)
```

```commandline
[100, 2, 3, 4, 5, 6, 7]
```

## Copy list

```python
digits = [1, 2, 3]

digits_2 = digits.copy()
digits_2.append(4)
print(digits_2)
print(digits)
```

```commandline
[1, 2, 3, 4]
[1, 2, 3]
```
> :warning:  Do not copy list using ```=```
> 
> It will just copy reference to list. Not values


- Regexp
- PyQT, Tkinter
- 