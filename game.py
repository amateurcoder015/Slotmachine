#gamble

import random

MAX_LINES = 3
MIN_LINES=1
MAX_BET = 100
MIN_BET = 1 

ROWS = 3
COLS = 3

symbol_count={
    'A':3,
    'B':4,
    'C':6,
    'D':8
}

symbol_value={
    'A':5,
    'B':4,
    'C':3,
    'D':2
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_line=[]
    for line in range(lines):
        symbol= columns[0][line]
        for column in columns:
            symbol_to_check= column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings+= values[symbol]*bet
            winning_line.append(line+1)
    return winnings, winning_line



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
        
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value= random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()



def deposit():
    while True:
        amount = input("please enter the amount you want to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("please enter a valid amount above 0")
        else:
            print("please enter a valid number")
    return amount

def get_number_of_lines():
    while True:
        line = input(F"please enter the amount of lines you want to bet on between {MIN_LINES} and {MAX_LINES}: ")
        if line.isdigit():
            line = int(line)
            if 1<=line<=MAX_LINES:
                break
            else:
                print(f"please enter a valid number between ${MIN_LINES} and ${MAX_LINES}")
        else:
            print("please enter a valid number")
    return line

def get_bet():
    while True:
        bet = input(f"enter the bet amount on EACH line between ${MIN_BET} and ${MAX_BET}: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print(f"please enter a valid amount above ${MIN_BET} and below ${MAX_BET}")
        else:
            print("please enter a valid number")
    return bet

def spin(balance):
    line = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*line
        if total_bet>balance:
            print(f"you do not have enough money for the desired bet, your current balance is {balance}")
            add_money=int(input("would you like to add more money: enter 1 for yes and 2 for no"))
            if add_money==1:
                balance+=deposit()
            else:
                print("then please change your bet according to your balance")
        else:
            break
    print(f"You are betting ${bet} on {line} lines. Total bet is equal to: ${total_bet}")
    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_line = check_winnings(slots,line,bet,symbol_value)
    print(f"you won ${winnings}.")
    print(f"You won on the lines:", *winning_line)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("press enter to play (q to quit)")
        if answer == 'q':
            break
        balance += spin(balance)
    print(f"you are left with ${balance}")

main()
