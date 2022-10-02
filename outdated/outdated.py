def main():
    while True:
        date = input("Date: ").strip()
        if to_iso_date(date):
            break

def to_iso_date(date):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    try:
        if date.find('/') != -1:
            date_list = date.split('/')
            m, d, y = (date_list[0]), (date_list[1]), (date_list[2])
            #print(m,d,y)
            if m.isdigit() and d.isdigit() and y.isdigit():
                m, d, y = int(date_list[0]), int(date_list[1]), int(date_list[2])

                if m > 12 or m < 1 or d > 31 or d < 1:
                    return False
                print(f"{y}-{m:02}-{d:02}")
                return True
        elif date.find(',') != -1:
            date = date.replace(',', '')
            date_list = date.split(' ')
            m, d, y = (date_list[0]), (date_list[1]), (date_list[2])
            if m.isalpha() and d.isdigit() and y.isdigit():
                d, y = int(date_list[1]), int(date_list[2])
                if d > 31 or d < 1:
                    return False
            index = months.index(m.title()) + 1
            #m = months[index]
            print(f"{y}-{index:02}-{d:02}")
            return True
    except IndexError:
        # print("index error")
        print("")

    except ValueError:
        # print("value error")
        print("")

    return False

main()