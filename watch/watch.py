import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    # if matches := re.search(r"https?://(?:www\.)?youtube\.com/embed/([a-z0-9_]+)", s, re.IGNORECASE):
    #     print(f"Username:", matches.group(1))
# <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

    if matches := re.search(r"iframe.+https?://(?:www\.)?youtube\.com/embed/([a-z0-9_]+)", s, re.IGNORECASE):
        id = matches.group(1)
        # print(id)
        return "https://youtu.be/" + id
    else:
        return None

if __name__ == "__main__":
    main()