## Fibonacci sequence

```python
# Fibonacci sequence


number = int(input('Enter: '))

# Fn = Fn-1 + Fn-2

num1 = 0
num2 = 1

next_number = num2

while next_number <= number:
    print(next_number, end=' ')
    num1, num2 = num2, next_number
    next_number = num1 + num2
```

```python
# Fibonacci sequence


number = int(input('Enter: '))

# Fn = Fn-1 + Fn-2

num1 = 0
num2 = 1

next_number = num2
count = 1

while count <= number:
    print(next_number, end=' ')
    num1, num2 = num2, next_number
    next_number = num1 + num2
    count += 1
```

## Module import

- Import whole module using ```import``` keyword

```python
import random

print(random.randint(1, 10))
print(random.choice([1, 2, 3]))
```

- Import something from module using ```from``` keyword

```python
from random import choice, randint
from math import sqrt

print(randint(1, 10))
print(choice([1, 2, 3]))

print(sqrt(25))
```

- Rename module using alias ```as```

```python
import turtle as t

t.forward(10)
t.left(90)
```