#Name: Claude Watson
#UID: U72087839
#The Price is Right (One Bid) - To determine the closest value to the price of a prize and select a winner.

import random

price = random.randint(1000,5000)

bid1 = int(input("Player 1, enter your bid:"))
bid2 = int(input("Player 2, enter your bid:"))
bid3 = int(input("Player 3, enter your bid:"))
bid4 = int(input("Player 4, enter your bid:"))

if bid1 > price and bid2 > price and bid3 > price and bid4 > price:
    print("Everyone overbid. Game over")
elif bid1 == price or bid2 == price or bid3 == price or bid4 == price:
    print("Someone guessed it right on the money!")

if bid1 == price:
    winner = "Player 1"
    print(f"Actual price is ${price}!", winner, "come on down!")
elif bid2 == price:
    winner = "Player 2"
    print(f"Actual price is ${price}!", winner, "come on down!")
elif bid3 == price:
    winner = "Player 3"
    print(f"Actual price is ${price}!", winner, "come on down!")
elif bid4 == price:
    winner = "Player 4"
    print(f"Actual price is ${price}!", winner, "come on down!")

if bid1 < price and bid2 < price and bid3 < price and bid4 < price:
    winner = max(bid1, bid2, bid3, bid4)
    if winner == bid1:
        print(f"Actual price is ${price}! Player 1 come on down!")
    elif winner == bid2:
        print(f"Actual price is ${price}! Player 2 come on down!")
    elif winner == bid3:
        print(f"Actual price is ${price}! Player 3 come on down!")
    elif winner == bid4:
        print(f"Actual price is ${price}! Player 4 come on down!")

if bid1 > price > bid2 and price > bid3 and price > bid4:
    winner = max(bid2, bid3, bid4)
    if winner == bid2:
        print(f"Actual price is ${price}! Player 2 come on down!")
    elif winner == bid3:
        print(f"Actual price is ${price}! Player 3 come on down!")
    elif winner == bid4:
        print(f"Actual price is ${price}! Player 4 come on down!")

if bid2 > price > bid1 and price > bid3 and price > bid4:
    winner = max(bid1, bid3, bid4)
    if winner == bid1:
        print(f"Actual price is ${price}! Player 1 come on down!")
    elif winner == bid3:
        print(f"Actual price is ${price}! Player 3 come on down!")
    elif winner == bid4:
        print(f"Actual price is ${price}! Player 4 come on down!")

if bid3 > price > bid2 and price > bid1 and price > bid4:
    winner = max(bid2, bid1, bid4)
    if winner == bid2:
        print(f"Actual price is ${price}! Player 2 come on down!")
    elif winner == bid1:
        print(f"Actual price is ${price}! Player 1 come on down!")
    elif winner == bid4:
        print(f"Actual price is ${price}! Player 4 come on down!")

if bid4 > price > bid2 and price > bid3 and price > bid1:
    winner = max(bid2, bid1, bid3)
    if winner == bid2:
        print(f"Actual price is ${price}! Player 2 come on down!")
    elif winner == bid1:
        print(f"Actual price is ${price}! Player 1 come on down!")
    elif winner == bid3:
        print(f"Actual price is ${price}! Player 3 come on down!")

if bid4 > price and bid2 > price and price > bid3 and price > bid1:
    winner = max(bid1, bid3)
    if winner == bid1:
        print(f"Actual price is ${price}! Player 1 come on down!")
    elif winner == bid3:
        print(f"Actual price is ${price}! Player 3 come on down!")

if bid1 > price and bid3 > price and price > bid2 and price > bid4:
    winner = max(bid2, bid4)
    if winner == bid2:
        print(f"Actual price is ${price}! Player 2 come on down!")
    elif winner == bid4:
        print(f"Actual price is ${price}! Player 4 come on down!")

if bid1 > price and bid2 > price and price > bid3 and price > bid4:
    winner = max(bid3, bid4)
    if winner == bid3:
        print(f"Actual price is ${price}! Player 3 come on down!")
    elif winner == bid4:
        print(f"Actual price is ${price}! Player 4 come on down!")

if bid1 > price and bid4 > price and price > bid2 and price > bid3:
    winner = max(bid2, bid3)
    if winner == bid2:
        print(f"Actual price is ${price}! Player 2 come on down!")
    elif winner == bid3:
        print(f"Actual price is ${price}! Player 3 come on down!")

if bid2 > price and bid3 > price and price > bid1 and price > bid4:
    winner = max(bid1, bid4)
    if winner == bid1:
        print(f"Actual price is ${price}! Player 1 come on down!")
    elif winner == bid4:
        print(f"Actual price is ${price}! Player 4 come on down!")

if bid3 > price and bid4 > price and price > bid2 and price > bid1:
    winner = max(bid2, bid1)
    if winner == bid2:
        print(f"Actual price is ${price}! Player 2 come on down!")
    elif winner == bid1:
        print(f"Actual price is ${price}! Player 1 come on down!")

if bid1 > price and bid2 > price and bid3 > price and price > bid4:
        print(f"Actual price is ${price}! Player 4 come on down!")

if bid4 > price and bid2 > price and bid3 > price and price > bid1:
        print(f"Actual price is ${price}! Player 1 come on down!")

if bid1 > price and bid4 > price and bid3 > price and price > bid2:
        print(f"Actual price is ${price}! Player 2 come on down!")

if bid1 > price and bid2 > price and bid4 > price and price > bid3:
        print(f"Actual price is ${price}! Player 3 come on down!")