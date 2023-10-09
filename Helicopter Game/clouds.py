from utils import randbool


class Clouds:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]

    def update(self, r=1, mxr=20, g=1, mxg=10):
        for i in range(self.height):
            for j in range(self.width):
                if randbool(r, mxr):
                    self.cells[i][j] = 1
                    if randbool(g, mxg):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0
