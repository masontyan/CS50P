def main():
    amount_due = 50
    coin = is_coin_valid(amount_due)
    new_amount_due = amount_due - coin

    while new_amount_due > 0:
        coin = is_coin_valid(new_amount_due)
        new_amount_due = new_amount_due - coin

    if new_amount_due < 0:
        print(f"Change Owed: {new_amount_due * -1}")
    else:
        print("Change Owed: 0")

def is_coin_valid(amount_due):

    while True:
        coin = int(input(f"Amount Due: {amount_due}\nInsert Coin: "))
        if coin == 25:
            return coin
        elif coin is 10:
            return coin
        elif coin is 5:
            return coin

main()

# #def main():
#     amount_due = 50

#     while amount_due > 0:
#         print(f"Amount Due: {amount_due}")
#         coin = int(input("Insert Coin: "))

#         if coin == 25 or coin == 10 or coin == 5:
#             amount_due = amount_due - coin

#     print(f"Change Owed: {amount_due * -1}")


# main()
