lower_bound = int(input('Enter: '))
upper_bound = int(input('Enter: '))

if lower_bound > upper_bound:
    lower_bound = lower_bound + upper_bound
    upper_bound = lower_bound - upper_bound
    lower_bound = lower_bound - upper_bound

i = lower_bound

while i < upper_bound:
    if (i + 5) % 7 == 0:
        print(i)

    i += 1

if lower_bound > upper_bound:
    while upper_bound < lower_bound:
        pass
elif upper_bound > lower_bound:
    while lower_bound < upper_bound:
        pass

