# Loops

## while

```python
number = 1

while number < 3:
    print(number)
    number += 1
```

```python
number = 1

limit = 3

while number < limit:
    number += 1
    print(number)
```

```python
x1 = int(input('Enter x1:'))
x2 = int(input('Enter x2:'))

sum = 0
x = x1  # Start

while x < x2:
    sum += x
    x += 1  # -> 1
    print('Sum: ', sum)

print('Sum between', x1, 'and', x2, 'is', sum)
```

```python
lower_bound = int(input('Enter: '))
upper_bound = int(input('Enter: '))

i = lower_bound

while i < upper_bound:
    if (i + 5) % 7 == 0:
        print(i)

    i += 1
```

```python
lower_bound = int(input('Enter: '))
upper_bound = int(input('Enter: '))

i = upper_bound

while lower_bound < i:
    if (i + 5) % 7 == 0:
        print(i)

    i -= 1
```

### Swap variables

```python
lower_bound = int(input('Enter: '))
upper_bound = int(input('Enter: '))

if lower_bound > upper_bound:
    lower_bound, upper_bound = upper_bound, lower_bound

i = lower_bound

while i < upper_bound:
    if (i + 5) % 7 == 0:
        print(i)

    i += 1
```

```python
lower_bound = int(input('Enter: '))
upper_bound = int(input('Enter: '))

if lower_bound > upper_bound:
    tmp = lower_bound
    lower_bound = upper_bound
    upper_bound = tmp

i = lower_bound

while i < upper_bound:
    if (i + 5) % 7 == 0:
        print(i)

    i += 1
```
---
### Factorial of a number
> **Task:** Calculate the factorial of a number ```n``` using a ```while``` loop.
> 
> **Example:** For ```n = 5```, the factorial is 120 (since ```5! = 5 * 4 * 3 * 2 * 1```).
---

[Examples](https://www.programiz.com/python-programming/examples/swap-variables)
---

# Additional tasks

1. Find prime numbers

> Task: Take from user start and end. Then display all prime numbers between start and end

2. Sum of digits in a Number

> **Task:** Write a program that takes an integer and uses a ```while``` loop to calculate the sum of its digits.
>
> **Example:** For the input ```123```, the output should be ```6```.
>
> **Hint:** Use modulo ```%``` to get the last digit and integer division ```//``` to remove the last digit in each
> loop.

3. Find the Smallest Divisor of a Number
> **Task:** Write a program to find the smallest divisor of a number greater than ```1```.
> 
> **Example:** For ```n = 15```, the output should be ```3``` (the smallest divisor other than ```1```).
> 
> **Hint:** Use a ```while``` loop to check each number staring from ```2``` until you find one that divides ```n``` with no remainder.