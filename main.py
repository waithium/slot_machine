#slot machine project
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8,
}



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

def get_bet():
    while True:
        bet = input(f'how much would you like to bet on each line?({MIN_BET}-{MAX_BET}): ')
        if bet.isdigit():
            bet =int(bet)
            if MIN_BET > bet or MAX_BET < bet:
                print(f"the number is out of range, the range is {MIN_BET}-{MAX_BET}")
                continue
            else:
                return bet
        else:
            print('please enter a number!!')
            print('-' * 22)

def main():
    while True:
        balance = deposit()
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines

        print(f"You are betting {bet}$ on {lines} lines. Your total bet is equal to {total_bet}. \n")
        if total_bet > balance:
            print("you don't have enough money for this bet!")
            action = input('do you wnat continue? (yes/no): ').lower()
            if action == 'yes':
                continue
            else:
                break

#play game
main()