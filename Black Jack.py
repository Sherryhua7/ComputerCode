import random
deckofcard = []
numberlist = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
suitlist = ['diamonds', 'hearts', 'clubs', 'spades']
player1score = 0
player2score = 0
for x in numberlist:
    for i in suitlist:
        deckofcard.append(str(x)+" of "+i)
print(deckofcard)

def player1():
    global player1score
    card = random.choice(deckofcard)
    deckofcard.remove(card)
    cardvalue = card[0:1]
    if cardvalue == 'J' or cardvalue == 'Q' or cardvalue == 'K':
        player1score += 10
    elif cardvalue == 'A':
        player1score += 1
    else:
        player1score += int(cardvalue)
    print("player1 got", card)
    print("the current score of player1 is", player1score)

def player2():
    global player2score
    card = random.choice(deckofcard)
    print(card)
    deckofcard.remove(card)
    cardvalue = card[0:1]
    if cardvalue == 'J' or cardvalue == 'Q' or cardvalue == 'K':
        player2score += 10
    elif cardvalue == 'A':
        player2score += 1
    else:
        player2score += int(cardvalue)
    print("player2 got", card)
    print("the current score of player2 is", player2score)

def wins():
    if player1score > player1score:
        print("player1 wins!")
    if player2score > player1score:
        print("player2 wins!")
    if player1score == player2score:
        print("a tie")


player1()
player1()
player2()
player2()

while True:
    if player1score < 21 or player2score < 21:
        play = input("add card? y/n")
        if play == "y":
            lengthoflist = len(deckofcard)
            if lengthoflist % 2 == 0:
                player1()
            else:
                player2()
        if play == "n":
            lengthoflist = len(deckofcard)
            if lengthoflist % 2 == 0:
                while True:
                    player2play = input("player2 add card? y/n")
                    if player2play == "y":
                        player2()
                        if player1score > 21:
                            print("player2 wins!")
                            break
                        if player2score > 21:
                            print("player1 wins!")
                            break
                        if player1score == 21:
                            print("player1 wins!")
                            break
                        if player2score == 21:
                            print("player2 wins!")
                            break
                    elif player2play == "n":
                        wins()
                        break
            else:
                while True:
                    player1play = input("player1 add card? y/n")
                    if player1play == "y":
                        player1()
                        if player1score > 21:
                            print("player2 wins!")
                            break
                        if player2score > 21:
                            print("player1 wins!")
                            break
                        if player1score == 21:
                            print("player1 wins!")
                            break
                        if player2score == 21:
                            print("player2 wins!")
                            break
                    elif player1play == "n":
                        wins()
                        break
    if player1score > 21:
        print("player2 wins!")
        break
    if player2score > 21:
        print("player1 wins!")
        break
    if player1score == 21:
        print("player1 wins!")
        break
    if player2score == 21:
        print("player2 wins!")
        break