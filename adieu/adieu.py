import inflect

def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("Input: ")
            names.append(name)


        except EOFError:
            break

    print(f"Adieu, adieu, to {p.join(names)}")
    
main()
