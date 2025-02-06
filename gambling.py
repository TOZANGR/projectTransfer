import os
import math as mt
import random
import time
import sys
def countTotal(list):
    list = filter(None, list)
    total = 0
    hasAce = False
    for card in list:
        if card == 'queen' or card == 'king' or card == 'jack':
               total += 10
        elif (card != 'ace'):
             total += int(card)
        else:
             hasAce = True
             total += 11
    if (total > 21) and (hasAce):
         total -= 10
    return total
def imMakingThisMethodToAvoidWritingOneReallyLongLineTwice(pointTotal, cards):
    return (input('would you like to hit or stand?\n') if int(pointTotal) < 21 else 'loss') if (int(pointTotal) != 21) and (len(cards) < 5) else 'win'

               
possibleCards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
os.system("clear")
machineList = {}
if (input("welcome to gamble time, would you like to play?\n") == 'blackjack'):
    money = 2000
    collector = open('./machineLearning.txt', 'a+')
    while (money > 100):
            seed = []
            for i in range(20):
                seed.append(random.randrange(0, len(possibleCards)))
            os.system('clear')
            cards = [possibleCards[seed[0]], possibleCards[seed[1]]]
            print(f'your cards are {cards}')
            pointTotal = str(countTotal(cards)) 
            userInput = imMakingThisMethodToAvoidWritingOneReallyLongLineTwice(pointTotal, cards)
            while userInput == 'hit':
                cards.append(possibleCards[seed[2]])
                os.system('clear')
                print(f'your cards are {cards}')
                pointTotal = str(countTotal(cards)) 
                userInput = imMakingThisMethodToAvoidWritingOneReallyLongLineTwice(pointTotal, cards)
                try:
                    machineList[pointTotal] += ', ' + userInput
                except:
                    machineList[pointTotal] = userInput            
            if userInput == 'end' or userInput == 'quit':
                collector.write(str(machineList))
                collector.close()
                sys.exit()
            try:
                machineList[pointTotal] += ', ' + userInput
            except:
                machineList[pointTotal] = userInput
            print(machineList)
            print(f'you ended with a total of {pointTotal}')
            time.sleep(2)