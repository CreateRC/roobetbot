from time import sleep
import random

#Variables and shit
rounds = []
bal_rounds = []
choice = 20.00 #initial start choice, we like 20
wins = 0
multi = 1.2

#Main container
def main(wins, rounds, multi, bal_rounds):
    print("Welcome to dice bot")
    sim_count = int(input("How many rolls to simulate> "))
    bal_start = int(input("What is the starting balance> "))
    bet = int(input("Enter bet size> "))               
    print("Starting 'roll over' choice: {}".format(choice))
    sleep(.5)
    print("Starting rolls...",end = "\r\n")
    sleep(1)

    #EVERY ROUND
    for _ in range(0, sim_count):
        if _ == 0:
            balance = bal_start
        else:
            balance = bal_rounds[-1]
        current_roll = roll()
        print("Rolled ~ {}".format(current_roll))
        rounds.append(current_roll)
              
        if current_roll > choice:
            wins = wins + 1
            new_balance = balance_calculator(balance, "win", bet, multi)
            bal_rounds.append(new_balance)
        else:
            new_balance = balance_calculator(balance, "loss", bet, multi)
            bal_rounds.append(new_balance)
        #sleep(.5)
    
    game_size = len(rounds)
    win_rate = round(wins / game_size, 2) * 100
    print("Win Percent >> {} / {} >> {}%".format(wins, game_size, win_rate))
    print("Ending balance >> ${}".format(bal_rounds[-1]))
    
#Start rolling
def roll():
    roll = random.uniform(0.00, 100.00)
    roll = round(roll, 2)
    return roll

def ai(roll, bet):
    #Adapt to the roll
    pass

def multiplier():
    for _ in range(.9949, 48.75):
        pass
    #ADD ALL MULTIS HERE LATER


def balance_calculator(balance, rType, bet, multi):
    balance -= bet
    if rType == "win":
        winnings = bet * multi
        balance = balance + winnings
    elif rType == "loss":
        pass

    return balance

main(wins, rounds, multi, bal_rounds)
    
