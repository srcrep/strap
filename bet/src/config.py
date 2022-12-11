#!/bin/python3

screen_height = int(input('Screen Hight (in pixels) : '))
screen_width = int(input('Screen Width (in pixels) : '))
payout_amount = float(input('Payout Amount : '))
bet_amount = float(input('Bet Amount : '))
loss_increase_percentage = int(input('Percentage Increase on Loss : '))
             
class Config: #800x600 currently... need to decide best way to take different resolutions
    def __init__(self, screen_height, screen_width):
        self
        self.payout_location = payout_location(screen_height, screen_width)
        self.payout_amount = payout_amount
        self.auto_bet_location = auto_bet_location(screen_height, screen_width)
        self.bet_amount_location = bet_amount_location(screen_height, screen_width)
        self.bet_amount = bet_amount
        self.enable_loss_increase_location = enable_loss_increase_location(screen_height, screen_width)
        self.loss_increase_location = loss_increase_location(screen_height, screen_width)
        self.loss_increase_percentage = loss_increase_percentage
        self.start_location = start_location(screen_height, screen_width)
        
    def payout_location(screen_height, screen_width):
        return
    def auto_bet_location(screen_height, screen_width):
        return
    def bet_amount_location(screen_height, screen_width):
        return
    def enable_loss_increase_location(screen_height, screen_width):
        return
    def loss_increase_location(screen_height, screen_width):
        return
    def start_location(screen_height, screen_width):
        return
