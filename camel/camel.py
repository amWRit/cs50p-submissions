def main():
    camel_case = input("camelCase: ")
    print(convert_to_snake(camel_case))



def convert_to_snake(camel_case):
    snake_case = ""
    for c in camel_case:
        if c.isupper():
            c = '_' + c.lower()
        snake_case = snake_case + c

    return snake_case

main()