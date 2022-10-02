import random


def main():
    lives = 3
    q_n = 10
    score = 0
    question = ""
    level = get_level()
    # print(level)
    while q_n > 0:
        x = generate_integer(level)
        y = generate_integer(level)
        sum = x + y

        while lives > -1:
            question = str(x) + ' + ' + str(y) + ' = '
            # answer = input(f"{q_n}: {question}")
            answer = input(question)
            try:
                if sum == int(answer):
                    score += 1
                    q_n -= 1
                    break
                    # if q_n == 10:
                    #     break
                else:
                    lives -= 1
                    print("EEE")
                    if lives == 0:
                        # print(f"{q_n}: {question} {answer}")
                        print(f"{question} {sum}")
                        lives = 3
                        q_n -= 1
                        break

            except ValueError:
                # lives -= 1
                print("EEE")

    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level in ['1', '2', '3']:
            return int(level)


# https://stackoverflow.com/a/2673399
def generate_integer(n):
    # range_start = 10**(n-1)
    # range_end = (10**n)-1
    # return random.randint(range_start, range_end)
    if n == 1:
        return random.randint(0, 9)
    elif n == 2:
        return random.randint(10, 99)
    elif n == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()