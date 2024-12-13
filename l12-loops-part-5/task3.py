import random

lower_bound = 0
upper_bound = 0
amount_of_questions = 0

difficulty_levels = {
    1: {
        'lower_bound': 1,
        'upper_bound': 10,
        'amount_of_questions': 5
    },
    2: {
        'lower_bound': 10,
        'upper_bound': 15,
        'amount_of_questions': 10
    }
}

while True:
    points = 0
    print('1. Ease')
    print('2. Medium')
    print('3. High')

    user_choice = int(input('Select: '))

    level = difficulty_levels.get(user_choice, None)
    if not level:
        print('Invalid choice!')
        continue

    for _ in range(level.get('amount_of_questions')):
        x = random.randint(level.get('lower_bound'), level.get('upper_bound'))
        y = random.randint(level.get('lower_bound'), level.get('upper_bound'))
        result = x * y

        print(x, '*', y, '=', end=' ')
        user_answer = int(input(''))

        if user_answer == result:
            points += 1
            print('Correct!')
        else:
            print('Incorrect')

    print('Result:', points)

#           *
#          * *
#         * * *
#        * * * *
#         * * *
#          * *
#           *

#           *
#          ***
#         *****
#        *******
#         *****
#          ***
#           *
