import pyautogui
import time

def loop():
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(1)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(120)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-', presses=5)
    time.sleep(60)
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
    """
    pyautogui.moveTo(x=102, y=166)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.write('0.0001')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    """
    pyautogui.click(x=75, y=360)
    time.sleep(1)
    pyautogui.moveTo(x=155, y=355)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.write('100000')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    return

def start():
    time.sleep(1)
    pyautogui.click(x=135, y=524)
    time.sleep(1)
    return

def speedmod():
    time.sleep(1)
    pyautogui.moveTo(x=374, y=496)
    time.sleep(5)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(x=405, y=496)
    time.sleep(5)
    pyautogui.click()
    time.sleep(1)
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
