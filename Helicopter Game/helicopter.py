from utils import randcell


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

    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if 0 <= nx < self.height and 0 <= ny < self.width:
            self.x, self.y = nx, ny

    def print_stats(self):
        print('🪣 ', self.tank, '/', self.mxtank, sep='', end=' | ')
        print('🏆', self.score)
