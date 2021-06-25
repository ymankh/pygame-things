import pygame as pg

WIDTH = 1000
HEIGHT = 500
window = pg.display.set_mode((WIDTH, HEIGHT))
points = []
run = True
scale = 500


def is_in_the_fractol(point):
    x, y = point
    c = complex(x, y)

    def f(z: complex):
        return z ** 2 + c

    z = c
    for _ in range(50):
        z = f(z)
        if z.imag ** 2 + z.real ** 2 > 1000:
            return False
    return True


def translate_point(point, x_translation, y_translation):
    return point[0] + x_translation, point[1] + y_translation


def transfear(point):
    return [int(point[i] * scale) for i in range(2)]


product = [[j / scale, i / scale] for i in range(int(-HEIGHT / 2), int(HEIGHT / 2)) for j in
           range(int(-WIDTH / 2), int(WIDTH / 2))]
for point in product:
    if is_in_the_fractol(point):
        points.append(transfear(point))

for point in points:
    window.set_at(translate_point(point, int(WIDTH / 2), int(HEIGHT / 2)), (225, 225, 225))
pg.display.flip()
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
pg.quit()

if __name__ == '__main__':
    pass
