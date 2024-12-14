import random

def spinRow():
    symbols = ['🍒', '⭐', '💰', '🍋', '🔔']
    result = [random.choice(symbols) for x in range(0, 3)]

    print("***************")

    for x in result:
        print(x, end=" | ")

    print()
    print("***************")

    return result

def getPayout(row, bet):
    bets = float(bet)
    if row[0] == row[1] and row[0] == row[2]:
        match row[0]:
            case '🍒':
                return bets * 2.0
            case '⭐':
                return bets * 5.0
            case '💰':
                return bets * 10.0
            case '🍋':
                return bets * 25.0
            case '🔔':
                return bets * 50.0
    else:
        return 0

print("*****************************")
print("Hello! Welcome to Willy Slots")
print("*****************************")

valid_balance = False
totalBalance = float(input("Enter your balance. "))

while not valid_balance:
    if totalBalance > 0:
        valid_balance = True
    else:
        print("Balance must be greater than 0. Try again")

valid_bet = False
bet = float(input("Enter bet amount. "))

while not valid_bet:
    if bet < 0:
        print("Bet must be greater than 0. Try again.")
    elif bet > totalBalance:
        print("Bet must be less than your total balance. Try again.")
    else:
        valid_bet = True

is_running = True

while is_running:
    if totalBalance <= 0:
        print("Ran out of funds. Sad day I guess")
        is_running = False
        break

    print(f"Current balance: ${totalBalance:.2f}")
    action = int(input("Enter 1 to spin or 2 to cash out."))

    if action == 1:
        totalBalance = totalBalance - bet
        result = spinRow()
        payout = float(getPayout(result, bet))

        totalBalance = totalBalance + payout

        
    elif action == 2:
        print(f"Final winnings: ${totalBalance:.2f}")
        is_running = False

    else:
        action = int(input("Invalid input. Try again."))







