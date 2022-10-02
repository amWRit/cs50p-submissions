def main():
    item = input("Enter item: ").lower()
    get_calories_of(item)


def get_calories_of(item):
    items = {
        "apple": "130",
        "avocado": "50",
        "banana": "110",
        "cantaloupe": "50",
        "grapefruit": "60",
        "grapes": "90",
        "honeydew melon": "50",
        "kiwifruit": "90",
        "lemon": "15",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "pineapple": "50",
        "plums": "70",
        "strawberroes": "50",
        "sweet cherries": "100",
        "tangerine": "50",
        "watermelon": "80",
    }

    if item in items:
        calories = items[item]cd
        print(f"Calories: {calories}")
    else:
        print("")

main()