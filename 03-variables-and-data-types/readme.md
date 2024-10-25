# Lesson 3. Variables and Data Types
---

## Principles

- DRY (Don't repeat yourself)

## Name conventions

- snake_case - my_name, sasha_dako
- kebab-case - first-name, upload-file
- SNAKE_UPPER_CASE - FIRST_NAME
- PascalCase - FirstName
- camelCase - firstName
- camelCase - firstName

##  Combined operators
```python
x = 2
x += 2
print(x)
```
```bash
4
```
---
```python
x = 2
x -= 2
print(x)
```
```bash
0
```
---
```python
x = 2
x *= 2
print(x)
```
```bash
4
```
---
```python
x = 2
x /= 2
print(x)
```
```bash
1
```
---
```python
x = 2
x **= 2
print(x)
```
```bash
4
```
---
```python
x = 2
x //= 2
print(x)
```
```bash
1
```
---
```python
x = 2
x %= 2
print(x)
```
```bash
0
```
---

## Hotkeys
- Ctrl + P - Показати аргументи функції (коли каретка всередині дужок функції)

---
```python
name = input('Enter your name: ')

print(name)
```
```bash
Enter your name: Sasha
Sasha
```
---
```python
# Concatenation
print('Hello ' + 'World')
```
---

```python
print(float('2.5'))
print(int('2'))
print(str(2))
```
---

```python
x = float(input('Enter x: '))
y = float(input('Enter y: '))

print(x + y)
```
```bash
Enter x: 5
Enter y: 5
10
```
---
```python
x: int = 3
name: str = 'Sasha'
```