from random import randint

redCards = ["rCard1", "rCard2", "rCard3", "rCard4", "rCard5", "rCard6", "rCard7", "rCard8", "rCard9", "rCard10"]

yellowCards = ["yCard1", "yCard2", "yCard3", "yCard4", "yCard5", "yCard6", "yCard7", "yCard8", "yCard9", "yCard10"]

blackCards = ["bCard1", "bCard2", "bCard3", "bCard4", "bCard5", "bCard6", "bCard7", "bCard8", "bCard9", "bCard10"]

cards = (blackCards, yellowCards, redCards)

p1 = 0
p2 = 0

p1name = input("Player 1 what is your name?")
p2name = input("Player 2 what is your name?")


p1pick = input("Press p to pick a card.")

if p1pick == "p":
    p1card = randint(blackCards, yellowCards, redCards)
    print(p1card)

p2pick = input("Press p to pick a card.")

if p2pick == "p":
    p2card = randint(blackCards, yellowCards, redCards)
    print(p2card)
