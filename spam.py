import pyautogui
import sys
import time
import random
import typing as t


class Spammer:
    def __init__(self) -> None:
        self._text = None
        self._count = None
        self._gibberish = None
        self._characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @property
    def text(self):
        if (self._text is None) or not(isinstance(self._text, str)) or not(isinstance(self._text, bytes)):
            # sys.exit("Please set a value to 'Spammer.text'!")
            pass
        return self._text

    @text.setter
    def text(self, value: t.Union[str, bytes, float, int]):
        self._text = str(value)

    @property
    def count(self):
        if (self._count is None) or not(isinstance(self._count, int)):
            print("Warning! 'Spammer.count' is not assigned, defaulting to 5")
            self._count = 5
        return self._count

    @count.setter
    def count(self, value: t.Union[str, int, float]):
        if isinstance(value, str):
            try:
                self._count = int(float(value))
            except ValueError:
                print("Warning! Invalid value for 'Spammer.count', defaulting to 5")
                self._count = 5
        else:
            self._count = int(value)

    @property
    def gibberish(self):
        if (self._gibberish is None) or not(isinstance(self._gibberish, int)):
            print("Warning! 'Spammer.gibberish' is not assigned, defaulting to 8")
            self._gibberish = 8
        return self._gibberish

    @gibberish.setter
    def gibberish(self,  value: t.Union[str, int, float]):
        if isinstance(value, str):
            try:
                self._gibberish = int(float(value))
            except ValueError:
                print("Warning! Invalid value for 'Spammer.gibberish', defaulting to 8")
                self._gibberish = 5
        else:
            self._gibberish = int(value)

    def _typeRandomCharacters(self) -> None:
        pyautogui.write(''.join(
            random.choice(
                self._characters
            ) for _ in range(self.gibberish)
        ))
        pyautogui.write(' ')

    def typeSentence(self, text: t.Union[str, bytes]) -> None:
        if isinstance(text, bytes):
            text = str(text)

        atStart = random.choice([True, False])

        if atStart:
            self._typeRandomCharacters()

        for word in text.split(' '):
            interval = float(str(random.uniform(0.15, 0.28))[:5])
            pyautogui.write(word, interval=interval)
            pyautogui.write(' ')
            time.sleep(interval/2)

        if not(atStart):
            self._typeRandomCharacters()

    def pressEnter(self) -> None:
        time.sleep(random.randint(3, 5))
        pyautogui.press('enter')

    def spam(self) -> None:
        print(
            f"[+] Number of Times: {self.count}\n[+] Number of gibberish: {self.gibberish}\n[+] Text: \n{self.text}\n\n")
        print('[*] Starting to spam in 3 seconds...')
        time.sleep(3)
        for count in range(1, self.count + 1):
            self.typeSentence(text=self.text)
            self.pressEnter()
            print(f'[{count}] Sent Message!')
