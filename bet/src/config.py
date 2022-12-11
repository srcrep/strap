#!/bin/python3

screen_width = int(input('Screen Hight (in pixels) : '))
screen_height = int(input('Screen Width (in pixels) : '))
payout_amount = float(input('Payout Amount : '))
bet_amount = float(input('Bet Amount : '))
loss_increase_percentage = int(input('Percentage Increase on Loss : '))
             
class Config: #800x600 currently... need to decide best way to take different resolutions
    def __init__(self, screen_width, screen_height):
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
        
    def auto_location(screen_width, screen_height):
        if screen_width == 800:
            if screen_height == 600:
                x = 196
                y = 151
                return x, y
            return x, y
        return x, y
    def payout_location(screen_width, screen_height):
        if screen_width == 800:
            if screen_height == 600:
                x = 275
                y = 311
                return x, y
            return x, y
        return x, y
    def bet_amount_location(screen_width, screen_height):
        if screen_width == 800:
            if screen_height == 600:
                x = 145
                y = 179
                return x, y
            return x, y
        return x, y
    def enable_loss_increase_location(screen_width, screen_height):
        if screen_width == 800:
            if screen_height == 600:
                x = 147
                y = 289
                return x, y
            return x, y
        return x, y
    def loss_increase_location(screen_width, screen_height):
        if screen_width == 800:
            if screen_height == 600:
                x = 187
                y = 289
                return x, y
            return x, y
        return x, y
    def ud_enable_loss_increase_location(screen_width, screen_height):
        if screen_width == 800:
            if screen_height == 600:
                x = 147
                y = 265
                return x, y
            return x, y
        return x, y
    def ud_loss_increase_location(screen_width, screen_height):
        if screen_width == 800:
            if screen_height == 600:
                x = 187
                y = 265
                return x, y
            return x, y
        return x, y
    def start_location(screen_width, screen_height):
        if screen_width == 800:
            if screen_height == 600:
                x = 176
                y = 371
                return x, y
            return x, y
        return x, y
