# Functions

Function - is named block of code created for reuse some code and add context tp program.

## Syntax

```python
def name_of_function():  # Must be verb
# Code
```

Example:

```python
def show_greetings():
    print('Hello!')


show_greetings()
```

Result:

```commandline
Hello!
```

## Functions with arguments

Functions can take any number of arguments and process them

Example:
```python
def show_title(title: str): # :str - type annotation
    print(title.capitalize().center(50, '-'))

show_title('hello')
show_title('GREETINGS')
show_title('Store')
show_title('SeTTings')
```
Result:
```commandline
----------------------Hello-----------------------
--------------------Greetings---------------------
----------------------Store-----------------------
---------------------Settings---------------------
```

Example:
```python
def show_sum(a: int, b: int, c: int):
    print(a + b + c)


x = 5
y = 2
z = 3

show_sum(x, y, z)
show_sum(x, y, 5)
show_sum(1, 7, 10)
```

## Function with ```return``` statement

```python
def convert_to_fahrenheit(celsius: float):
    return (celsius * 9 / 5) + 32


print(convert_to_fahrenheit(50))
f = convert_to_fahrenheit(50)

print('Result: ', f * 5 / 2)
```

Functions can contain multiple ```return``` statements
```python
def is_even_or_odd(number: int):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


print(is_even_or_odd(2)) # Even
print(is_even_or_odd(3)) # Odd
```