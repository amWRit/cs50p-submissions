def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        # print("bad length")
        return False
    elif not is_alpha_digit(s):
        # print("bad character")
        return False
    elif not s[0:2].isalpha():
        # print("bad starting char")
        return False
    elif starts_zero(s):
        # print("digit starts with zero")
        return False
    elif not valid_trailing_digit(s):
        # print("bad trailing digit")
        return False
    else:
        return True

def is_alpha_digit(plate):
    for c in plate:
        if not c.isalpha() and not c.isdigit():
            return False
    return True

def starts_zero(plate):
    for c in plate:
        if c.isalpha():
            continue
        elif c.isdigit():
            if c == '0':
                return True
            else:
                return False
    return False

def valid_trailing_digit(plate):
    for index, c in enumerate(plate):
        if c.isdigit():
            for i in range(index + 1, len(plate) - 1):
                if plate[i].isalpha():
                    return False
    return True

main()