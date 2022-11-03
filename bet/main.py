import pyautogui
import time

def loop():
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(0.1)
    pyautogui.write('surf bc.game/game/classic-dice')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(15)
    with pyautogui.hold('ctrl'):
        pyautogui.press('-', presses=5)
    time.sleep(0.5)
    pyautogui.doubleClick(x=296, y=372)
    time.sleep(0.5)
    pyautogui.write('4.95')
    time.sleep(0.5)
    pyautogui.click(x=173, y=123)
    time.sleep(0.5)
    pyautogui.doubleClick(x=98, y=165)
    time.sleep(0.5)
    pyautogui.write('0.0001')
    time.sleep(0.5)
    pyautogui.click(x=69, y=360)
    time.sleep(0.5)
    pyautogui.doubleClick(x=152, y=358)
    time.sleep(0.5)
    pyautogui.write('25')
    time.sleep(0.5)
    pyautogui.click(x=136, y=524)
    return

def speedmod():
    pyautogui.click(x=374, y=496)
    time.sleep(0.25)
    pyautogui.click(x=405, y=496)
    time.sleep(0.5)
    return

def main():
    loop()
    time.sleep(1)
    speedmod()
    time.sleep(1)
    for _ in range(10):
        loop()
        return
    return

main()

    
    
