#!/bin/python3

screen_width = 800 # int(input('Screen Hight (in pixels) : '))
screen_height = 600 # int(input('Screen Width (in pixels) : '))
payout_amount = 99 # float(input('Payout Amount : '))
bet_amount = 0.0001 # float(input('Bet Amount : '))
loss_increase_percentage = 1.1 # int(input('Percentage Increase on Loss : '))
             
class Config: #800x600 currently... need to decide best way to take different resolutions

    def __init__(self, screen_width, screen_height):
        self
        self.classic_dice(screen_height, screen_width) = classic_dice(screen_height, screen_width)
        self.limbo(screen_height, screen_width) = limbo(screen_height, screen_width)
        self.ultimate_dice(screen_height, screen_width) = ultimate_dice(screen_height, screen_width)

    def classic_dice(screen_height, screen_width):

        def auto_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 197
                    y = 151
                    return x, y
                return x, y
            return x, y

        def payout_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 277
                    y = 311
                    return x, y
                return x, y
            return x, y

        def bet_amount_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 150
                    y = 177
                    return x, y
                return x, y
            return x, y

        def enable_loss_increase_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 139
                    y = 294
                    return x, y
                return x, y
            return x, y

        def loss_increase_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 178
                    y = 292
                    return x, y
                return x, y
            return x, y

        def start_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 172
                    y = 372
                    return x, y
                return x, y
            return x, y

    def limbo(screen_height, screen_width):

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
                    x = 269
                    y = 328
                    return x, y
                return x, y
            return x, y

        def bet_amount_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 145
                    y = 178
                    return x, y
                return x, y
            return x, y

        def enable_loss_increase_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 141
                    y = 294
                    return x, y
                return x, y
            return x, y

        def loss_increase_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 178
                    y = 294
                    return x, y
                return x, y
            return x, y

        def start_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 170
                    y = 373
                    return x, y
                return x, y
            return x, y

    def ultimate_dice(screen_height, screen_width):

        def auto_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 198
                    y = 151
                    return x, y
                return x, y
            return x, y

        def payout_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 271
                    y = 332
                    return x, y
                return x, y
            return x, y

        def bet_amount_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 149
                    y = 178
                    return x, y
                return x, y
            return x, y

        def enable_loss_increase_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 146
                    y = 266
                    return x, y
                return x, y
            return x, y

        def loss_increase_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 186
                    y = 266
                    return x, y
                return x, y
            return x, y

        def start_location(screen_width, screen_height):
            if screen_width == 800:
                if screen_height == 600:
                    x = 168
                    y = 372
                    return x, y
                return x, y
            return x, y