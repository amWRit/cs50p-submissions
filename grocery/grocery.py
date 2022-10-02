def main():
    grocery = {}

    while True:
        try:
            item = input("").upper()

            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1

        except EOFError:
            break
    #print(grocery)
    #sorted_grocery = dict(sorted(grocery.items(), key=lambda item: item[1], reverse = True))
    sorted_grocery = sorted(grocery)
    #print(sorted_grocery)
    for key in sorted_grocery:
        print(f"{grocery[key]} {key}")

main()
