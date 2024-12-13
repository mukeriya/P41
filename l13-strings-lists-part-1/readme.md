# Strings

N = 2^b

N - Потужність алфавіту
b - кількість біт для представлення символу

```python
user_message = 'Hello і'

user_message_enc = user_message.encode('utf-8')

print(user_message_enc)

user_message_dec = user_message_enc.decode('windows-1251')
print(user_message_dec)
```

```bash
b'Hello \xd1\x96'
Hello С–
```

```python
message = 'Hello world!'

print(id(message))

message += 'asdasd'

print(id(message))
```

```python
message = 'hello'
message_2 = 'hello'

print(id(message) == id(message_2))

print(id(message))
print(id(message_2))
```

## Literals

```python
message = 'Hello'
message_2 = "Hello"
message_3 = '''
Hello
'''

message_4 = """
Hello' " " '
"""
```

```python
message = 'foobar'

print(message[0])  # f
print(message[1])  # o
print(message[-1])  # r - Last symbol

# print(message[::-1])  # raboof
```

```python
str1 = 'Hello '
str2 = 'Admin'

print(id(str1 + str2))
str3 = str1 + str2
print(id(str3)) 

# Duplicate

print('*' * 5) # *****

message = 'Hello'

print(len(message)) # 5
```


## Slices

```python
message = 'Hello world!'

print(message[5:10])  # worl
print(message[5:])  # world!
print(message[:10])  # Hello worl
print(message[:200])  # Hello world!
print(message[10:5])  #
print(message[-1:5])  #
print(message[::2])  # Hlowrd
print(message[2:-2:2])  # lowr
print(message[::-1])  # lowr
```

## Register

```python
message = 'python was created in the late 1980`s by Guido van Rossum.'

print(message.lower())  # python was created in the late 1980`s by guido van rossum.
print(message.upper())  # PYTHON WAS CREATED IN THE LATE 1980`S BY GUIDO VAN ROSSUM.
print(message.capitalize())  # Python was created in the late 1980`s by guido van rossum.
print(message.title())  # Python Was Created In The Late 1980`S By Guido Van Rossum.
print(message.swapcase())  # PYTHON WAS CREATED IN THE LATE 1980`S BY gUIDO VAN rOSSUM.
```


```python
message = 'python was created in the late 1980`s by Guido van Rossum.'

print(message.count('python'))  # 1
print(message.count('python', 20, 65))  # 0
print(message.count('python', 10))  # 0

print(message.find('a'))  # 8
print(message.find('і'))  # -1
print(message.rfind('a'))  # 48

print(message.index('a'))  # 8
print(message.rindex('a'))  # 48
print(message.rindex('і'))  # Exception
```

## Search methods

```python
message = 'python was created in the late 1980`s by Guido van Rossum.'

print(message.count('python'))  # 1
print(message.count('python', 20, 65))  # 0
print(message.count('python', 10))  # 0

print(message.find('a'))  # 8
print(message.find('і'))  # -1
print(message.rfind('a'))  # 48

print(message.index('a'))  # 8
print(message.rindex('a'))  # 48
print(message.rindex('і'))  # Exception
```


## String checks

```python
message = 'python was created in the late 1980`s by Guido van Rossum.'

print(message.startswith('P'))  # False
print(message.startswith('p'))  # True
print(message.startswith('python'))  # True
print(message.endswith('.'))  # True
print(message.endswith('!'))  # False
print(message.endswith('!'))  # False

print(message.isalnum())  # False
print(message.isalpha())  # False
print(message.isdigit())  # False
print('4'.isdigit())  # True
print(message.islower())  # False
print(message.isupper())  # False
print(message.isspace())  # False
print(message.istitle())  # False
```


## Formatting

```python
message = 'Python2024'

print(message.center(50))  # Python2024
print(message.center(50, '*'))  # ********************Python2024********************
print(message.center(5))  # Python2024

message = 'Python\t\t2024'

print(message)
print(message.expandtabs(8))
print(message.expandtabs())

print(message.ljust(50))
print(message.ljust(50, '@'))

print(message.rjust(50))
print(message.rjust(50, '@'))

message = ' Python '

print(message.lstrip())
print(message.rstrip())
print(message.strip())
print(message.strip(' P'))

number = '123'

print(number.zfill(5))

number = "+123"

print(number.zfill(5))

print('Hello\nworld')  # new line
print('Hello\bworld')  # backspace
print('Hello\rworld')  # return caret
print('Hello\tworld')  # tab

print('\x2C')
print('\053')
print('\'')
print('\"')
print('\\')
print(r'\asda \n')
```

# Additional tasks
> Підрахунок голосних у строці


Напишіть програму,яка рахує кількість голосних літер у строці

```bash
Enter: Hello world!
Result: 3
```
---
> Анаграма

Напишіть програму, яка перевіряє, чи є дві строка анаграмами (містять однакові символи у різному порядку)

```bash
Enter first word: listen
Enter second word: silte
Result: True

Enter first word: cat
Enter second word: dog
Result: False
```
---
> Підрахунок кількості слів

Напишіть програму, яка рахує кількість слів у строці

```bash
Enter: Hello world!
Result: 2
```

