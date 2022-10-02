import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]
    try:
        file_ext = file_name.split('.')[1]
        if  file_ext != "py":
            sys.exit("Not a Python file")
    except IndexError:
        sys.exit("Not a Python file")

    try:
        with open(file_name) as file:
            lines = file.readlines()
            # print(lines)
    except FileNotFoundError:
        sys.exit()

    count = get_lines_count(lines)
    print(count)

def get_lines_count(lines):
    count = 0
    for line in lines:
        line = line.lstrip().rstrip()
        # print(line)
        if not line.startswith("#") and not line == '':
            count += 1

    return count

if __name__ == "__main__":
    main()