import sys
import csv
from tabulate import tabulate

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    menu = []

    file_name = sys.argv[1]
    try:
        file_ext = file_name.split('.')[1]
        if  file_ext != "csv":
            sys.exit("Not a CSV file")
    except IndexError:
        sys.exit("Not a CSV file")

    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            for pizza, small, large in reader:
                menu.append([pizza, small, large])

    except FileNotFoundError:
        sys.exit("File doesn't exist!")

    print(tabulate(menu, headers="firstrow", tablefmt="grid"))



if __name__ == "__main__":
    main()