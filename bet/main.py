import pyautogui
import time
from time import sleep
from tqdm import trange
from os import system

def pause(a):
    for i in trange(a):
        sleep(1)
        os.system('clear')
    return

def main():

    time.sleep(1)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(1)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(1)
    pyautogui.press('enter')
    pause(120)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-', presses=6)
    pause(120)
    pyautogui.moveTo(x=232, y=372)
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('4.95')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=139, y=117)
    time.sleep(3)
    pyautogui.click(x=60, y=358)
    time.sleep(1)
    pyautogui.moveTo(x=146, y=360)
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.write('25')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    time.sleep(1)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(1)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(1)
    pyautogui.press('enter')
    pause(120)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-', presses=6)
    pause(120)
    pyautogui.moveTo(x=232, y=372)
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('4.95')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x=345, y=375)
    time.sleep(3)
    pyautogui.click(x=139, y=117)
    time.sleep(3)
    pyautogui.click(x=60, y=358)
    time.sleep(1)
    pyautogui.moveTo(x=146, y=360)
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.write('25')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    time.sleep(1)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(1)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(1)
    pyautogui.press('enter')
    pause(120)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-', presses=6)
    pause(120)
    pyautogui.moveTo(x=232, y=372)
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('1.2375')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=139, y=117)
    time.sleep(3)
    pyautogui.click(x=60, y=358)
    time.sleep(1)
    pyautogui.moveTo(x=146, y=360)
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.write('25')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    time.sleep(1)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(1)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(1)
    pyautogui.press('enter')
    pause(120)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-', presses=6)
    pause(120)
    pyautogui.moveTo(x=232, y=372)
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('1.2375')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x=345, y=375)
    time.sleep(3)
    pyautogui.click(x=139, y=117)
    time.sleep(3)
    pyautogui.click(x=60, y=358)
    time.sleep(1)
    pyautogui.moveTo(x=146, y=360)
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.write('25')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    return
main() 