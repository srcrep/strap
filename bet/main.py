import pyautogui
import time
from time import sleep
from tqdm import trange
from os import system

amt = '0.001'

def pause(a):
    for i in trange(a):
        sleep(1)
        system('clear')
    return

def main():
    #first
    time.sleep(3)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(3)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(3)
    pyautogui.press('enter')
    pause(120)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-', presses=6)
    pause(120)
    pyautogui.moveTo(x=232, y=372) # change payout
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('4.95')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=139, y=117) # click auto
    time.sleep(3)
    pyautogui.moveTo(x=80, y=165) #input amount location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(amt) #input amount
    time.sleep(3)
    pyautogui.click(x=60, y=358) # on auto
    time.sleep(3)
    pyautogui.moveTo(x=146, y=360) # on auto amount
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('25')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=107, y=541) # start

    ##second
    time.sleep(3)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(3)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(3)
    pyautogui.press('enter')
    pause(120)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-', presses=6)
    pause(120)
    pyautogui.moveTo(x=232, y=372) # change payout
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('4.95')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=, y=) # change bet direction
    time.sleep(3)
    pyautogui.click(x=139, y=117) # click auto
    time.sleep(3)
    pyautogui.moveTo(x=80, y=165) #input amount location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(amt) #input amount
    time.sleep(3)
    pyautogui.click(x=60, y=358) # on auto
    time.sleep(3)
    pyautogui.moveTo(x=146, y=360) # on auto amount
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('25')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=107, y=541) # start

    #third
    time.sleep(3)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(3)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(3)
    pyautogui.press('enter')
    pause(120)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-', presses=6)
    pause(120)
    pyautogui.moveTo(x=232, y=372) # change payout
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('1.2375')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=139, y=117) # click auto
    time.sleep(3)
    pyautogui.moveTo(x=80, y=165) #input amount location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(amt) #input amount
    time.sleep(3)
    pyautogui.click(x=60, y=358) # on auto
    time.sleep(3)
    pyautogui.moveTo(x=146, y=360) # on auto amount
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('250')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=107, y=541) # start

    ##fourth
    time.sleep(3)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(3)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(3)
    pyautogui.press('enter')
    pause(120)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-', presses=6)
    pause(120)
    pyautogui.moveTo(x=232, y=372) # change payout
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('1.2375')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=, y=) # change bet direction
    time.sleep(3)
    pyautogui.click(x=139, y=117) # click auto
    time.sleep(3)
    pyautogui.moveTo(x=80, y=165) #input amount location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(amt) #input amount
    time.sleep(3)
    pyautogui.click(x=60, y=358) # on auto
    time.sleep(3)
    pyautogui.moveTo(x=146, y=360) # on auto amount
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('250')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=107, y=541) # start

main() 