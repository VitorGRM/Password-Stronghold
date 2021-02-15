import os
import time


def Clean():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
def TextAnimatio (text):
    Clean()
    x = 0
    shown_text = ""
    while x < len(text):
        Clean()
        shown_text += text[x]
        print(shown_text)
        x += 1
        time.sleep(0.00000000000000001)
