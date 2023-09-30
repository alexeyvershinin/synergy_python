# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - магазин апгрейдов

CELL_TYPES = '🟩🌲🌊🏥🛠'


class Map:

    def generate_rivers(self):
        pass

    def generate_forest(self):
        pass

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
tmp.print_map()
