#!/bin/python3

import pyautogui
import time
from time import sleep
from tqdm import trange
from os import system
from config import Config as config

payout_amount = config.payout_amount
bet_amount = config.bet_amount
loss_increase_percentage = config.loss_increase_percentage

def pause(a):
    for i in trange(a):
        sleep(1)
        system('clear')
    return

classic_dice_payout_location = config.classic_dice.payout_location
classic_dice_auto_bet_location = config.classic_dice.auto_bet_location
classic_dice_bet_amount_location = config.classic_dice.bet_amount_location
classic_dice_enable_loss_increase_location = config.classic_dice.enable_loss_increase_location
classic_dice_loss_increase_location = config.classic_dice.loss_increase_location
classic_dice_start_location = config.classic_dice.start_location

def classicDice():
    #bcgame classic-dice
    time.sleep(3)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(3)
    pyautogui.write('chromium bc.game/game/classic-dice --new-window')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.moveTo(classic_dice_payout_location) # change payout
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(payout_amount)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(classic_dice_auto_bet_location) # click auto
    time.sleep(3)
    pyautogui.moveTo(classic_dice_bet_amount_location) #input amount location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(bet_amount) #input amount
    time.sleep(3)
    pyautogui.click(classic_dice_enable_loss_increase_location) # on auto
    time.sleep(3)
    pyautogui.moveTo(classic_dice_loss_increase_location) # on auto amount
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(loss_increase_percentage)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(classic_dice_start_location) # start

limbo_payout_location = config.limbo.payout_location
limbo_auto_bet_location = config.limbo.auto_bet_location
limbo_bet_amount_location = config.limbo.bet_amount_location
limbo_enable_loss_increase_location = config.limbo.enable_loss_increase_location
limbo_loss_increase_location = config.limbo.loss_increase_location
limbo_start_location = config.limbo.start_location

def limbo():
    #bcgame classic-dice
    time.sleep(3)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(3)
    pyautogui.write('chromium bc.game/game/limbo --new-window')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.moveTo(limbo_payout_location) # change payout
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(payout_amount)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(limbo_auto_bet_location) # click auto
    time.sleep(3)
    pyautogui.moveTo(limbo_bet_amount_location) #input amount location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(bet_amount) #input amount
    time.sleep(3)
    pyautogui.click(limbo_enable_loss_increase_location) # on auto
    time.sleep(3)
    pyautogui.moveTo(limbo_loss_increase_location) # on auto amount
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(loss_increase_percentage)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(limbo_start_location) # start

ultimate_dice_payout_location = config.ultimate_dice.payout_location
ultimate_dice_auto_bet_location = config.ultimate_dice.auto_bet_location
ultimate_dice_bet_amount_location = config.ultimate_dice.bet_amount_location
ultimate_dice_enable_loss_increase_location = config.ultimate_dice.enable_loss_increase_location
ultimate_dice_loss_increase_location = config.ultimate_dice.loss_increase_location
ultimate_dice_start_location = config.ultimate_dice.start_location

def ultimateDice():
    #bcgame classic-dice
    time.sleep(3)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    time.sleep(3)
    pyautogui.write('chromium bc.game/game/limbo --new-window')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.moveTo(ultimate_dice_payout_location) # change payout
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(payout_amount)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(ultimate_dice_auto_bet_location) # click auto
    time.sleep(3)
    pyautogui.moveTo(ultimate_dice_bet_amount_location) #input amount location
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(bet_amount) #input amount
    time.sleep(3)
    pyautogui.click(ultimate_dice_enable_loss_increase_location) # on auto
    time.sleep(3)
    pyautogui.moveTo(ultimate_dice_loss_increase_location) # on auto amount
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.write(loss_increase_percentage)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(ultimate_dice_start_location) # start


def main():
    classicDice()
    limbo()
    ultimateDice()
    