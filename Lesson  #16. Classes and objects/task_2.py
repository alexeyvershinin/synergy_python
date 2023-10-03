def main():
    class Turtle:
        def __init__(self, x=0, y=0, s=1):
            self.x = x
            self.y = y
            self.s = s

        def go_up(self):
            self.y += self.s

        def go_down(self):
            self.y -= self.s

        def go_left(self):
            self.x -= self.s

        def go_right(self):
            self.x += self.s

        def evolve(self):
            self.s += 1

        def degrade(self):
            if self.s > 1:
                self.s -= 1
            else:
                raise ValueError("S не может быть меньше или равно 0")

        def count_moves(self, x2, y2):
            distance_x = abs(self.x - x2)
            distance_y = abs(self.y - y2)

            moves = (distance_x + distance_y) / self.s

            if moves > int(moves):
                return f'Черепашке потребуется {int(moves) + 1} шагов, чтобы добраться до ({x2}, {y2})'
            else:
                return f'Черепашке потребуется {int(moves)} шагов, чтобы добраться до ({x2}, {y2})'

    turtle = Turtle()

    turtle.go_right()
    turtle.evolve()
    turtle.go_up()
    turtle.go_up()
    turtle.go_left()

    print(f'Текущая позиция: ({turtle.x}, {turtle.y})')
    print(f'Текущее s: {turtle.s}')
    print(turtle.count_moves(3, 5))


if __name__ == "__main__":
    main()