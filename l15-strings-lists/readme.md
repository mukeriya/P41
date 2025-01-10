# Lists

```python
users = ['Petro']  # init list
users.append('Sasha')  # add element
users.append('Hello')
users.pop()  # remove last element and get it
users.pop(0)  # remove element by id and get it
users.remove('Sasha')  # remove element by value
users.index('Sasha')  # get element index by value
users_copy = users.copy()  # copy list
users.reverse()  # reverse list
users.extend(['Hello', 'World'])  # extend list with another list

# union 2 lists
print([1, 2, 3] + [4, 5, 6])  # [1,2,3,4,5,6]
first_half = [1, 2, 3]
second_half = [4, 5, 6]
print(first_half + second_half)  # [1,2,3,4,5,6]

another_list = ['Hello', 'World']
users.extend(another_list)  # extend list with another list
users.insert(0, 'Petro')  # insert element in some position
```

## Tuple

```Tuple``` - is a immutable version of list

### Initialization

```python
admins = ('admin1', 'admin2')
admins = 'admin1', 'admin2'
admins = ('admin1',)
admins = 'admin1',
admins = tuple(['Hello'])

another_list = ['Hello']
admins = tuple(another_list)
```

## Set

### Initialization

```python
elements = {}
elements = {1, 2, 3}
elements = set()
elements = set([1, 2, 3])
```

### Set operations

```python
x = {1, 2, 3, 4, 5}
y = {4, 5, 6, 7, 8}

print(x.intersection(y))  # {4, 5}
print(x.difference(y))  # {1, 2, 3}
print(y.difference(x))  # {6, 7, 8}
print(x.symmetric_difference(y))  # {1, 2, 3, 6, 7, 8}
print(x.union(y))  # {1, 2, 3, 4, 5, 6, 7, 8}

print(x & y)  # intersection            # {4, 5}
print(x - y)  # difference              # {1, 2, 3}
print(y - x)  # difference              # {6, 7, 8}
print(x ^ y)  # symmetric_difference    # {1, 2, 3, 6, 7, 8}
print(x | y)  # union                   # {1, 2, 3, 4, 5, 6, 7, 8}
```

Every ```set operations``` has version with ```_update``` postfix. Works the same way but updates original list

- ```.intersection_update```
- ```.difference_update```
- ```.symmetric_difference_update```

### Set checks

```python
x = {1, 2, 3, 4, 5, 6, 7}
y = {3, 4, 5}

print(x.issubset(y))  # False
print(y.issubset(x))  # True
print(y.issuperset(x))  # False
print(x.issuperset(y))  # True
```

### Difference between ```.remove()``` and ```.discard()```

Difference is that ```.remove()``` raises exception if value does not exists in list, but ```.discard()``` just ignores

```python
x = {1, 2, 3}

x.remove(3)  # Works Fine!

print(x)  # {1,2}
```

```python
x = {1, 2, 3}

x.remove(4)  # Raise exception

print(x)  
```

```python
x = {1, 2, 3}

x.discard(3)  # Works Fine!

print(x)  # {1,2}
```

```python
x = {1, 2, 3}

x.discard(4)  # Works fine!

print(x)  # {1, 2, 3}
```

### isdisjoint

```python
x = {1, 2, 3}
y = {4, 5, 6}

print(x.isdisjoint(y))  # True

x = {1, 2, 3, 4}
y = {4, 5, 6, 7}

print(x.isdisjoint(y))  # False
```