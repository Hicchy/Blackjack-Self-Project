from random import random
from classes import *

# TODO number of players
# TODO deck
# TODO player decks
# TODO drawing cards and removing them from the deck
# TODO Ace is 1 is sum > 21
# TODO Compare the decks
# TODO Choose a winner


# TODO dict of cards with card: cardName and score: cardScore

numPlayers = int(input("How many players? Min. 1, Max. 5  ")) + 1
players = []
playerCards = [players]

sums = []
deck = CardDeck()
deck.makeDeck()
continues = True
hasLost = False
dealerHand = []


def makePlayer(name):
    player = Player()
    player.name = name
    return player.name


def makeDecks():
    for x in range(1, numPlayers):
        qqq = input(f"Name of player {x}?  ").lower()
        players.append({"name": makePlayer(qqq), "cards": []})
    print("\n")




def draw():

    for i in range(len(players)):
        drawn = random.choice(deck.deck)
        players[i]['cards'].append(drawn)
        deck.deck.remove(drawn)



def checkSums1():
    val1 = players[player]['cards'][0]['score']
    val2 = players[player]['cards'][1]['score']
    sum1 = val1 + val2
    if sum1 > 21:
        if val1 == 11:
            players[player]['cards'][0]['score'] = 1
        elif val2 == 11:
            players[player]['cards'][1]['score'] = 1


def checkSums2():
    val1 = players[player]['cards'][0]['score']
    val2 = players[player]['cards'][1]['score']
    sum1 = val1 + val2
    if len(players[player]['cards']) == 3:
        val3 = players[player]['cards'][2]['score']
        sum2 = val1 + val2 + val3
        if sum2 > 21:
            if val3 == 11:
                players[player]['cards'][2]['score'] = 1
                pass

    if sum1 > 21:
        if val1 == 11:
            players[player]['cards'][0]['score'] = 1
        elif val2 == 11:
            players[player]['cards'][1]['score'] = 1


def compare():
    for num in range(len(players)):
        val1 = players[num]['cards'][0]['score']
        val2 = players[num]['cards'][1]['score']
        if len(players[num]['cards']) == 3:
            val3 = players[num]['cards'][2]['score']
            sum = val1 + val2 + val3
            if sum > 21:
                return False
        elif len(players[num]['cards']) == 2:
            sum = val1 + val2
            if sum > 21:
                return False





def decide():
    compare()
    for playe in range(len(players)):
        if compare():
            isWinner = True
        elif not compare():
            isWinner = False
            return isWinner



def winner():
    end = False
    while not end:
        cursor = 0
        if decide():
            for comp in range(len(players)):
                pName = players[play]['name'].title()
                val1 = players[comp]['cards'][0]['score']
                val2 = players[comp]['cards'][1]['score']
                sum = 0

                if len(players[comp]['cards']) == 3:
                    val3 = players[comp]['cards'][2]['score']
                    sum = val1 + val2 + val3
                elif len(players[comp]['cards']) == 2:
                    sum = val1 + val2

                if cursor > comp:
                    print(f"{pName} lost with the hand {players[comp]['cards']}")
                    cursor = comp
                elif cursor < comp:
                    print(f"{pName} won with the hand {players[comp]['cards']}")
                    cursor = comp
                    end = True

    continues = False




















while continues:
    makeDecks()
    players.append({"name": "dealer", "cards": []})
    draw()
    draw()
    for player in range(len(players)):
        pName = players[player]['name'].title()
        card1 = players[player]['cards'][0]['card']
        card2 = players[player]['cards'][1]['card']
        if pName == "Dealer":
            print(f"{pName}: {card1} ??")
        else:
            print(f"{pName}: {card1} {card2}")
    checkSums1()
    for play in range(len(players)):
        pName = players[play]['name'].title()
        if pName == "Dealer":
            val1 = players[play]['cards'][0]['score']
            val2 = players[play]['cards'][1]['score']
            sum1 = val1 + val2
            if sum1 < 17:
                drawn = random.choice(deck.deck)
                players[play]['cards'].append(drawn)
                deck.deck.remove(drawn)
        else:
            ques = input(f"{pName}, draw or pass?  [ d / p] ").lower()
            if ques == "d":
                drawn = random.choice(deck.deck)
                players[play]['cards'].append(drawn)
                deck.deck.remove(drawn)
    checkSums2()
    for play in range(len(players)):
        pName = players[play]['name'].title()
        card1 = players[play]['cards'][0]['card']
        card2 = players[play]['cards'][1]['card']
        if len(players[play]['cards']) == 3:
            card3 = players[play]['cards'][2]['card']
            print(f"{pName}: {card1} {card2} {card3}")
        else:
            print(f"{pName}: {card1} {card2}")
    winner()
    continues = False














