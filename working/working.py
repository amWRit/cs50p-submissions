import re
import sys


def main():
    print(convert(input("Hours: ")))

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# convert("9 AM to 5 PM") == "09:00 to 17:00"
# convert("10:30 PM to 8:50 AM") == "22:00 to 08:00"
def convert(s):
    if matches := re.search(r"^([1][0-2]|[0]?[1-9])(?:\:)?([0-5][0-9]|[60])? (AM|PM) to ([1][0-2]|[0]?[1-9])(?:\:)?([0-5][0-9]|[60])? (AM|PM)$", s):
        hours1 = int(matches.group(1))
        minutes1 = matches.group(2)
        am_pm1 = matches.group(3)
        if am_pm1 == "PM":
            if hours1 != 12:
                hours1 = hours1 + 12
        elif am_pm1 == "AM" and hours1 == 12:
            hours1 = 0

        hours2 = int(matches.group(4))
        minutes2 = matches.group(5)
        am_pm2 = matches.group(6)
        if am_pm2 == "PM":
            if hours2 != 12:
                hours2 = hours2 + 12
        elif am_pm2 == "AM" and hours2 == 12:
            hours2 = 0

        if minutes1 is None:
            minutes1 = 0
        else:
            minutes1 = int(minutes1)
        if minutes2 is None:
            minutes2 = 0
        else:
            minutes2 = int(minutes2)

        return(f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}")


    else:
        raise ValueError("")

if __name__ == "__main__":
    main()