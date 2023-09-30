from utils import randbool, randcell, randcell2

# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - магазин апгрейдов

CELL_TYPES = '🟩🌲🌊🏥🛠'


class Map:

    def generate_river(self, length):
        rc = randcell(self.width, self.height)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while length > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx2, ry2):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                length -= 1

    def generate_forest(self, r, mxr):
        for ri in range(self.height):
            for ci in range(self.width):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def print_map(self):
        print('⬛' * (self.width + 2))
        for row in self.cells:
            print('⬛', end='')
            for cell in row:
                if 0 <= cell <= len(CELL_TYPES):
                    print(CELL_TYPES[cell], end='')
            print('⬛')
        print('⬛' * (self.width + 2))

    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.height or y >= self.width:
            return False
        return True

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]


tmp = Map(20, 10)
# tmp.generate_forest(3, 10)
tmp.generate_river(10)
tmp.print_map()
