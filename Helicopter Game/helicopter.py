from utils import randcell
import os


class Helicopter:
    def __init__(self, width, height):
        rc = randcell(width, height)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.height = height
        self.width = width
        self.mxtank = 1
        self.tank = 0
        self.score = 0
        self.lives = 20

    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if 0 <= nx < self.height and 0 <= ny < self.width:
            self.x, self.y = nx, ny

    def print_stats(self):
        print('🪣 ', self.tank, '/', self.mxtank, sep='', end=' | ')
        print('🏆', self.score, end=' | ')
        print('❤️', self.lives)

    def game_over(self):
        os.system('clear')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('X                                     X')
        print('X    GAME OVER, YOUR SCORE IS', self.score, '    X')
        print('X                                     X')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        exit(0)

    def export_data(self):
        return {
            'score': self.score,
            'lives': self.lives,
            'x': self.x,
            'y': self.y,
            'tank': self.tank,
            'mxtank': self.mxtank
        }

    def import_data(self, data):
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.tank = data['tank'] or 0
        self.mxtank = data['mxtank'] or 1
        self.lives = data['lives'] or 20
        self.score = data['score'] or 0
