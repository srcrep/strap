#!/bin/python3

import pyautogui
import time
from time import sleep
from tqdm import trange
from os import system
from config import Config as config

payout_location = config.payout_location
payout_amount = config.payout_amount
auto_bet_location = config.auto_bet_location
bet_amount_location = config.bet_amount_location
bet_amount = config.bet_amount
enable_loss_increase_location = config.enable_loss_increase_location
loss_increase_location = config.loss_increase_location
loss_increase_percentage = config.loss_increase_percentage
start_location = config.start_location

def pause(a):
    for i in trange(a):
        sleep(1)
        system('clear')
    return

def main():
    #bcgame classic-dice
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
    pyautogui.moveTo(change_payout_location) # change payout
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(payout_amount)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(auto_bet_location) # click auto
    time.sleep(3)
    pyautogui.moveTo(bet_amount_location) #input amount location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(bet_amount) #input amount
    time.sleep(3)
    pyautogui.click(enable_loss_increase_location) # on auto
    time.sleep(3)
    pyautogui.moveTo(loss_increase_location) # on auto amount
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(loss_increase_percentage)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(start_location) # start
main()