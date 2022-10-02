import sys
from PIL import Image, ImageOps

def main():
    check_cmd_args(3)

    students = []

    file_before = sys.argv[1].lower()
    file_after = sys.argv[2].lower()

    check_file_ext(file_before, file_after, ["jpg", "jpeg", "png"])

    try:
        image_before = Image.open(file_before)
        shirt = Image.open("shirt.png")
        size = shirt.size
        image_before = ImageOps.fit(image_before, size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        image_before.paste(shirt, shirt)
        image_before.save(file_after)

    except FileNotFoundError:
        sys.exit("File doesn't exist!")

def check_cmd_args(n):
    if len(sys.argv) < n:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > n:
        sys.exit("Too many command-line arguments")

def check_file_ext(file_before, file_after, acceptable_ext):
    try:
        file_before_ext = file_before.split('.')[1]
        file_after_ext = file_after.split('.')[1]
        # print(file_before_ext)
        # print(file_after_ext)

        if  file_before_ext not in acceptable_ext or file_after_ext not in acceptable_ext:
            sys.exit("Invalid input")
        if file_before_ext != file_after_ext:
            sys.exit("Input and output have different extensions.")

    except IndexError:
        sys.exit("Invalid input")

if __name__ == "__main__":
    main()