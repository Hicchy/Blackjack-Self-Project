import random



class Player:



    def __init__(self):
        self.name = ""


class CardDeck:


    def __init__(self):
        self.deck = []


    def addHearts(self):
        for x in range(2, 11):
            name = "h" + str(x)
            self.deck.append({"card": name, "score": x})
        self.deck.append({"card": "hA", "score": 11})
        self.deck.append({"card": "hJ", "score": 10})
        self.deck.append({"card": "hQ", "score": 10})
        self.deck.append({"card": "hK", "score": 10})


    def addSpades(self):
        for x in range(2, 11):
            name = "s" + str(x)
            self.deck.append({"card": name, "score": x})
        self.deck.append({"card": "sA", "score": 11})
        self.deck.append({"card": "sJ", "score": 10})
        self.deck.append({"card": "sQ", "score": 10})
        self.deck.append({"card": "sK", "score": 10})


    def addDimes(self):
        for x in range(2, 11):
            name = "d" + str(x)
            self.deck.append({"card": name, "score": x})
        self.deck.append({"card": "dA", "score": 11})
        self.deck.append({"card": "dJ", "score": 10})
        self.deck.append({"card": "dQ", "score": 10})
        self.deck.append({"card": "dK", "score": 10})


    def addClubs(self):
        for x in range(2, 11):
            name = "c" + str(x)
            self.deck.append({"card": name, "score": x})
        self.deck.append({"card": "cA", "score": 11})
        self.deck.append({"card": "cJ", "score": 10})
        self.deck.append({"card": "cQ", "score": 10})
        self.deck.append({"card": "cK", "score": 10})


    def makeDeck(self):
        self.addHearts()
        self.addClubs()
        self.addSpades()
        self.addDimes()

