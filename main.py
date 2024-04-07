#slot machine project
MAX_LINES = 3

def deposit():
    while True:
        amount = input('please enter your bet: \n$')
        if amount.isdigit():
            amount =int(amount)
            if amount <= 0:
                print('your bet should be above zero!')
                continue
            else:
                return amount
        else:
            print('please enter a number!!')
            print('-' * 22)

def get_number_of_lines():
    while True:
        limit = input(f'please enter the number of lines you want to bet on(1 - {MAX_LINES}): ')
        if limit.isdigit():
            limit =int(limit)
            if 1 > limit or  limit > MAX_LINES:
                print(f"the number is out of range, the range is 1 - {MAX_LINES}")
                continue
            else:
                return limit
        else:
            print('please enter a number!!')
            print('-' * 22)

