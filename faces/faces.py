def convert(text):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

def main():
    text = input("Enter a text:")
    text = convert(text)
    print(f"{text}")

main()