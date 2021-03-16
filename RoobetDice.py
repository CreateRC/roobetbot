from time import sleep
import random

def welcome(choice):
    print("Welcome to dice bot")
    sim_count = int(input("How many rolls to simulate> "))
    bal_start = int(input("What is the starting balance> "))
    bet = int(input("Enter bet size> "))               
    print("Starting 'roll over' choice: {}".format(choice))
    sleep(.5)
    print("Starting rolls...",end = "\r\n")
    sleep(1)

    return sim_count, bal_start, bet

#Main container
def main():
    #Variables and shit
    choice = 20.00 #initial start choice, we like 20
    sim_count, bal_start, bet = welcome(choice)
    rounds = []
    bal_rounds = []
    rStatus = []
    wins = 0
    multi = 1.2

    #EVERY ROUND
    for _ in range(0, sim_count):
        #Round check for balance fix
        if _ == 0:
            balance = bal_start
        else:
            balance = bal_rounds[-1]
            
        current_roll = roll()
        print("Rolled ~ {}".format(current_roll))
        rounds.append(current_roll)
              
        if current_roll > choice:
            wins = wins + 1
            rType = "win"
            new_balance = balance_calculator(balance, rType, bet, multi)
            bal_rounds.append(new_balance)
            
        else:
            rType = "loss"
            new_balance = balance_calculator(balance, rType, bet, multi)
            bal_rounds.append(new_balance)
        #sleep(.5)

        #Give a helping hand (brain) to the bot
        if rType == "win" or "loss":
            rStatus.append(rType)
        else:
            print("Something whack, you nulled")

        #Feed the bot the info
        ai_intake(choice, current_roll, bet, rStatus)
        
    game_size = len(rounds)
    win_rate = round(wins / game_size, 2) * 100
    print("Win Percent >> {} / {} >> {}%".format(wins, game_size, win_rate))
    print("Ending balance >> ${}".format(bal_rounds[-1]))
    
def roll():
    roll = random.uniform(0.00, 100.00)
    roll = round(roll, 2)
    return roll

def ai_intake(choice, roll_generated, bet, rStatus):
    #rStatus is the bot memory
    rolled = roll_generated
    choice = choice
    bet = bet

    #Send to bot brain
    what_do = ai_react(choice, rolled, bet, rStatus)


def ai_react(choice, rolled, bet, rStatus):
    #Print current game that the bot knows
    print("Choice> {} _ Bet> ${} _ Outcome> {}\n".format(choice, bet, rStatus[-1]))

    #Figure out what to do next after learning last choices
    
    
        

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

main()
    
