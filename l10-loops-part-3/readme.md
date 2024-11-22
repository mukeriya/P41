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