import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid Usage")

if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid Usage")

    if sys.argv[2] not in fonts:
        sys.exit("Invalid Usage")

    else:
        font = sys.argv[2]

if len(sys.argv) == 1:
    font = (random.choice(fonts))

text = input("Input: ")

figlet.setFont(font=font)

result = figlet.renderText(text)

print(result)
