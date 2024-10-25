# Strings

```python
greetings = 'Hello'
print(greetings)
print(greetings[4])
```
```bash
Hello
H
```
---
```python
name = input('Enter your name: ')

print(name)

print(name[0])
print(len(name))
print(len(name) * 2)
print(type(len(name)))
```

```bash
Enter your name: Sasha
Sasha
S
10
<class 'int'>
```
---
```python
name = input('Enter your name: ')

print(name)

print(name[0])
print(name[-1])
```

```bash
Enter your name: Sasha
Sasha
S
a
```

## Tasks
- Площа та периметр прямокутника
Прийміть 2 (висота та ширина) дробних числа та потрібно обрахувати площу та периметр прямокутника
```bash
Enter height: 5
Enter width: 5

Area: 25
Perimeter: 20 
```
- Середнє арифметичне
Потрібно прийняти три числа (a, b, c) від користувача та вирахувати їх середнє арифметичне

```bash
Enter a: 2.5
Enter b: 3
Enter c: 15

Average: ...
```

- Калькулятор ступенів
Потрібно прийняти від користувача число та ступінь та вивести результат приведення до ступеня

```bash
Enter base: 5
Enter exponent: 2

Results: 25
```