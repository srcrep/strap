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
    pyautogui.moveTo(x=232, y=372)
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('4.95')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=139, y=117)
    time.sleep(3)
    pyautogui.moveTo(x=80, y=165) #input amount location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(amt) #input amount
    time.sleep(3)
    pyautogui.click(x=60, y=358)
    time.sleep(3)
    pyautogui.moveTo(x=146, y=360)
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('25')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=107, y=541)
"""
#first lowest rdp res 800 x 600
    time.sleep(3)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(3)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(3)
    pyautogui.press('enter')
    pause(15)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-', times=6)
    pause(15)
    pyautogui.moveTo(x=523, y=582) #payout location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('4.95') #payout amount
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=312, y=177) #turn on auto
    time.sleep(3)
    pyautogui.moveTo(x=168, y=251) #input amount location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(amt) #input amount
    time.sleep(3)
    pyautogui.click(x=145, y=560) #click "on-lose" to enable
    time.sleep(3)
    pyautogui.moveTo(x=261, y=563) #"on-lose" percentage increase location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('25') #"on-lose" percentage increase amount
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=243, y=770) #start

#second
    time.sleep(3)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(3)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(3)
    pyautogui.press('enter')
    pause(120)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-')
    pause(120)
    pyautogui.moveTo(x=523, y=582) #payout location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('4.95') #payout amount
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=721, y=585)
    time.sleep(3)
    pyautogui.click(x=312, y=177) #turn on auto
    time.sleep(3)
    pyautogui.moveTo(x=168, y=251) #input amount location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(amt) #input amount
    time.sleep(3)
    pyautogui.click(x=145, y=560) #click "on-lose" to enable
    time.sleep(3)
    pyautogui.moveTo(x=261, y=563) #"on-lose" percentage increase location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('25') #"on-lose" percentage increase amount
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=243, y=770) #start

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
        pyautogui.press('-')
    pause(120)
    pyautogui.moveTo(x=523, y=582) #payout location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('1.2375') #payout amount
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=312, y=177) #turn on auto
    time.sleep(3)
    pyautogui.moveTo(x=168, y=251) #input amount location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(amt) #input amount
    time.sleep(3)
    pyautogui.click(x=145, y=560) #click "on-lose" to enable
    time.sleep(3)
    pyautogui.moveTo(x=261, y=563) #"on-lose" percentage increase location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('850') #"on-lose" percentage increase amount
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=243, y=770) #start

#forth
    time.sleep(3)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(3)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(3)
    pyautogui.press('enter')
    pause(120)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-')
    pause(120)
    pyautogui.moveTo(x=523, y=582) #payout location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('1.2375') #payout amount
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=721, y=585)
    time.sleep(3)
    pyautogui.click(x=312, y=177) #turn on auto
    time.sleep(3)
    pyautogui.moveTo(x=168, y=251) #input amount location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(amt) #input amount
    time.sleep(3)
    pyautogui.click(x=145, y=560) #click "on-lose" to enable
    time.sleep(3)
    pyautogui.moveTo(x=261, y=563) #"on-lose" percentage increase location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write('850') #"on-lose" percentage increase amount
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=243, y=770) #start
"""

main() 
