import pyautogui
import os
import time
import random
import typing as t


class Spammer:
    def __init__(self) -> None:
        self._count = None
        self._text = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value: t.Union[str, int, float]):
        if isinstance(value, str):
            try:
                self._count = float(value)
            except ValueError:
                print("Warning! Invalid value for 'count', defaulting to 5")
                self._count = 5  # default to 5
        else:
            self._count = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value: t.Union[str, float, int, bytes]):
        self._text = str(value)

    def typeSentence(self, text: t.Optional[str] = None) -> None:
        for word in text.split(" "):
            interval = float(str(random.uniform(0.15, 0.5))[:5])
            pyautogui.write(word, interval=interval)
            pyautogui.write(" ")
            time.sleep(interval/2)

    def run(self) -> None:
        for count in range(1, self._count):
            self.typeSentence(text=self._text)
            pass


obj = Spammer()
obj.count = 'gfdrgd'
