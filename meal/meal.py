def main():
    time = input("What time is it? ")
    val = convert(time)

    #
    # print(val)

    print(check_what_to_eat(val))


def convert(time):
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = float(minutes)

    return hours + minutes/60

#  breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00
def check_what_to_eat(val):
    if 7 <= val <= 8:
        return "breakfast time"
    elif 12 <= val <= 13:
        return "lunch time"
    elif 18 <= val <= 19:
        return "dinner time"
    else:
        return ""

if __name__ == "__main__":
    main()