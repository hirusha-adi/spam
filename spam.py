import pyautogui
import os
import time
import random
import typing as t


def typeSentence(text: t.Optional[str] = None):
    for word in text.split(" "):
        interval = float(str(random.uniform(0.15, 0.5))[:5])
        pyautogui.write(word, interval=interval)
        pyautogui.write(" ")
