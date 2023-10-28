import random
from art import logo
print(logo)
flag = True


def givecard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def compare(a, b):
    sum_a = sum(a)
    sum_b = sum(b)
    sum_a = 21-sum_a
    sum_b = 21-sum_b
    print(f"Dealer Cards Are {b}")
    print(f"My Cards Are {a}")
    if sum_b > sum_a:
        print("YOU WIN!!!!")
    elif sum_b < sum_a:
        print("YOU LOSED!!!")
    elif sum_a == sum_b:
        print("IT'S A DRAW!!")


while flag:

    print("\nDo You Want To Play BlackJack\n")
    play_or_not = input(("type 'yes' to Start and 'no' to exit : ")).lower()
    if play_or_not == "yes":

        # Here's our Code Begin
        mycard = []

        for n in range(2):
            mycard.append(givecard())

        print(f"You got {mycard}")

        print(f"Sum Of Your Cards Is : {mycard[0]+mycard[1]}")

        dealercard = []

        for n in range(2):
            dealercard.append(givecard())

        print(f"Dealer one card is {dealercard[1]}")

        if sum(dealercard) < 15:
            dealercard.append(givecard())

        print("do you want one more card ??? ")
        addmorecard = input(("type 'y' for yes and 'n' for no : ")).lower()
        if addmorecard == "y":
            mycard.append(givecard())
            if sum(mycard) > 21:
                print("Sum Of Your Card Exceeds 21 So,")
                print("You Losed ")
                break
            compare(mycard, dealercard)
        elif addmorecard == "n":
            compare(mycard, dealercard)
        else:
            print("Invalid Input")

    else:
        flag = False
