import math

def main():
    percent = get_fuel_percent("Fraction: ")
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")

def get_fuel_percent(prompt):
    while True:
        try:
            x, y = input(prompt).split('/')
            x, y = int(x), int(y)
            if x <= y:
                return round(x*100/y)
        except ValueError:
            print("x or y is not an integer")
        except ZeroDivisionError:
            print("x or y can't be zero")

main()