from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    dob = input("Date of Birth: ")
    if validate(dob):
        minutes = number_of_minutes(dob)
        print(minutes_into_words(minutes))

...
def validate(dob):
    matches = re.match(r"^\d{4}-([0][1-9]|[1][0-2])-([0][1-9]|[12][0-9]|[3][01])$", dob)
    # print(matches)
    if matches:
        return True
    else:
        # raise ValueError("Not a valid date")
        sys.exit("Not a valid date")

def number_of_minutes(dob, fake_date=False):
    if fake_date:
        current_date = date(2000,1,1)
    else:
        current_date = date.today()
    #for testing purpose
    # current_date = date(2000,1,1)
    dob = date.fromisoformat(dob)

    diff = current_date - dob
    days = diff.days
    return (days * 1440)

def minutes_into_words(minutes):
    # print(minutes)
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"

if __name__ == "__main__":
    main()