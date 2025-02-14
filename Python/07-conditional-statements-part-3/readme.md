# Conditional Statements
[Examples](https://www.geeksforgeeks.org/python-match-case-statement/)
```python
number = 2

match number:
    case 1:
        print('Hello')  # If
    case 3:
        print('Not hello')  # Elif
    case _:
        print('Default')  # Else
```

```python
letter = 'a'

match letter:
    case 'a':
        print('A')
    case 'b':
        print('B')
```
```python
weekday_number = int(input('Enter: '))

match weekday_number:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Day')
    case 4:
        print('Day')
    case 5:
        print('Day')
    case 6:
        print('Day')
    case 7:
        print('Day')
    case _:
        print('Invalid day')
```
```python
month_number = 2

match month_number:
    case 1 | 2 | 12:
        print('Winter')
    case 3 | 4 | 5:
        print('')
```