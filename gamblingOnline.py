import os
import math as mt
import random
import time
import sys
import requests as rq
import socket
from inputimeout import inputimeout, TimeoutOccurred
import asyncio
def countTotal(list):
    list = filter(None, list)
    total = 0
    hasAce = 0
    for card in list:
        if card == 'queen' or card == 'king' or card == 'jack':
               total += 10
        elif (card != 'ace'):
             total += int(card)
        else:
             hasAce += 1
             total += 11
    if (total > 21) and (hasAce > 0):
         for i in range(hasAce):
            total -= 10
    return total
def imMakingThisMethodToAvoidWritingOneReallyLongLineTwice(pointTotal, cards):
    return (input('would you like to hit or stand?\n') if int(pointTotal) < 21 else 'loss') if (int(pointTotal) != 21) and (len(cards) < 5) else 'win'

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def loading(ip):
    os.system('clear')
    while playercount['started'] == 'false':
        players = ((rq.get(f"http://127.0.0.1:8000/queue/{ip}").json()))

        playercount['started'] = players['started']
        print(f'waiting with {int(players['players']) - 1} other players', end='\r' if players['started'] == 'false' else "someone has started the game, beginning with {players} players")

        if playercount['players'] == 1:
            try:
                c = inputimeout(prompt='\n(you are host, enter start to start)\n', timeout=3)
            except TimeoutOccurred:
                c = 'timeout'
            if 's' in c:
                rq.get(f"http://127.0.0.1:8000/start/")
                break
            os.system('clear')
        time.sleep(1)
        

os.system("clear")
ip = get_ip()
playercount = (rq.get(f"http://127.0.0.1:8000/queue/{ip}")).json()
print(f'there are {playercount['players']} players currently queuing.\nif you are #1, you are the host\nand can start the game whenever everyone is ready.\nOtherwise, sit back and wait')
time.sleep(5)
loading(ip)
time.sleep(3)
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