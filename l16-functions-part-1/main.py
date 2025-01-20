users = {
    'admin': 10,
    'user': 5,
    'contact_info': {
        'address': 'aasd'
    }
}

print(users['admin'])
print(users['user'])

user = {
    'first_name': 'Oleg',
    'last_name': 'Olegovich',
    'contacts': {
        'phone': "53543",
        'address': 'Karpatska Ukraine st.'
    }
}

print(user['first_name'])
print(user['contacts'])
print(user['contacts']['phone'])

print(user.values())
print(user.keys())
print(user.items())

print('Values:')
for value in user.values():
    print(value)

print()

print('Keys:')

for key in user.keys():
    print(key)

print()

print('Records: ')

for key, value in user.items():
    print(key, value)

if 'first_name' in user.keys():
    print(user['first_name'])
else:
    print('Key not found')

print(user.get('asd'))
print(user.get('asd', 'Some value'))
print(user.get('first_name', 'Some value'))

print(user.setdefault('first_name', 5))


user['new field'] = 'Some value'

print(user)
