import sys
import csv
from tabulate import tabulate

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    students = []

    file_before = sys.argv[1]
    file_after = sys.argv[2]
    try:
        file_before_ext = file_before.split('.')[1]
        file_after_ext = file_after.split('.')[1]

        if  file_before_ext != "csv" or file_before_ext != "csv":
            sys.exit("Not a CSV file")

    except IndexError:
        sys.exit("Not a CSV file")

    try:
        with open(file_before) as file:
            reader = csv.DictReader(file)
            for row in reader:
                l, f = row["name"].strip().replace(' ','').split(',')
                # l, f = row["name"].lstrip().split(',')
                students.append({"first": f, "last": l, "house": row["house"]})
            # print(students)
            # students = sorted(students, key=lambda student: student["first"])
            # print(students)
    except FileNotFoundError:
        sys.exit("File doesn't exist!")

    # print(tabulate(students, headers="firstrow", tablefmt="grid"))

    try:
        with open(file_after, "w", newline='') as file:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for row in students:
                # print(row)
                writer.writerow(row)
                # writer.writerow({'first_name': row["first_name"], 'last_name': row["last_name"], 'house': row["name"]})
                # students.append({"name": row["name"], "house": row["house"]})

    except:
        sys.exit("Error")



if __name__ == "__main__":
    main()