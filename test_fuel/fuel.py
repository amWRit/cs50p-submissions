import math


def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(gauge(percent))

def convert(fraction):
    while True:
        x, y = fraction.split('/')
        x, y = int(x), int(y)
        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError
        elif x <= y:
            return int(round(x*100/y))
        # except ValueError:
        #     # print("x or y is not an integer")
        #     # break
        #     return
        # except ZeroDivisionError:
        #     print("x or y can't be zero")
        #     break

def gauge(percent):
    if percent <= 1:
        return("E")
    elif percent >= 99:
        return("F")
    else:
        return(f"{percent}%")

if __name__ == "__main__":
    main()