import random
import sys
from pyfiglet import Figlet

len = len(sys.argv)

if len != 1 and len != 3:
    sys.exit("Invalid Usage")

else:
    figlet = Figlet()
    fonts =  figlet.getFonts()

    if len == 1:
        text = input("Input: ")
        font = random.choice(fonts)
        figlet.setFont(font=font)
        print(f"Output: {figlet.renderText(text)}")

    elif len == 3:
        font = sys.argv[2]
        if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and font in fonts:
            text = input("Input: ")
            figlet.setFont(font=font)
            print(f"Output: {figlet.renderText(text)}")
        else:
            sys.exit("Invalid Usage")