def main():
    due = 50
    global total
    total = 0
    while True:
        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            total += coin
        if  total >= 50:
            print(f"Change Owed: {total-50}")
            break
        else:
            due = 50 - total

main()