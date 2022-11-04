import pyautogui
import time
import sys

for i in xrange(10,0,-1):
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()
    time.sleep(1)

def loop():
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(1)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(1)
    pyautogui.press('enter')
    for i in xrange(120,0,-1):
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush()
        time.sleep(1)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-', presses=5)
    for i in xrange(60,0,-1):
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush()
        time.sleep(1)
    pyautogui.moveTo(x=314, y=389)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.write('1.0102')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x=174, y=119)
    time.sleep(1)
    pyautogui.click(x=75, y=360)
    time.sleep(1)
    pyautogui.moveTo(x=155, y=355)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.write('10000')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    print('loop')
    return

def start():
    time.sleep(1)
    pyautogui.click(x=135, y=524)
    time.sleep(1)
    print('start')
    return

def speedmod():
    time.sleep(1)
    pyautogui.moveTo(x=374, y=496)
    time.sleep(10)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(x=405, y=496)
    time.sleep(10)
    pyautogui.click()
    time.sleep(1)
    print('speedmod')
    return

def main():
    loop()
    time.sleep(1)
    speedmod()
    time.sleep(1)
    start()
    time.sleep(1)
    return

main()

for _ in range(4):
    time.sleep(1)
    loop()
    time.sleep(1)
    start()
