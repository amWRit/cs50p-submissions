def main():
    word = input("Input: ")
    print("Output:", shorten(word))


def shorten(word):
    output = ''
    for c in word:
        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            c = ''
        output += c
    return output


if __name__ == "__main__":
    main()


