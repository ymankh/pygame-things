import pygame as pg

# import os, sys
#
#
# def resource_path(relative_path):
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)
HEIGHT = 500
WIDTH = 900
window = pg.display.set_mode((WIDTH, HEIGHT))
FBS = 60
clock = pg.time.Clock()

run = True
GRAY = [200, 200, 200]
DARK_GRAY = [75, 75, 75]


class Button:
    def __init__(self, position: list, dimensions: list, color: list,
                 hover_color: list, **kwargs):
        self.hover_color = hover_color
        self.color = color
        self.dimensions = dimensions
        self.position = position
        self.hovering = False
        self.current_color = color
        self.transition_state = 0
        self.smoothness = 30
        for key in kwargs:
            if key == "smoothness":
                self.smoothness = kwargs[key]

    @staticmethod
    def smooth_transition(start: int, end: int, smoothness: int, i: int):

        amount_of_numbers = smoothness

        step = (end - start) / (amount_of_numbers - 1)

        number = 0

        i = i + 1

        if i == 1:
            number = start

        if i == 2:
            number = start + step

        if 3 <= i < amount_of_numbers:
            number = start + (i - 1) * step

        if i == amount_of_numbers:
            number = start + (amount_of_numbers - 1) * step

        return number

    def draw(self):
        self.change_color()
        pg.draw.rect(window, self.current_color, pg.Rect([*self.position, *self.dimensions]))

    def check_for_hovering(self, the_event: pg.event.Event):
        if the_event.type == pg.MOUSEMOTION:
            mouse_pos = pg.mouse.get_pos()
            x, y = mouse_pos
            x_pos_in = self.position[0] <= x <= self.position[0] + self.dimensions[0]
            y_pos_in = self.position[1] <= y <= self.position[1] + self.dimensions[1]
            self.hovering = x_pos_in and y_pos_in

    def change_color(self):
        sr, sg, sb = self.color
        tr, tg, tb = self.hover_color
        if self.hovering:
            if self.transition_state != self.smoothness - 1:
                self.transition_state += 1
            else:
                return
        else:
            if self.transition_state != 0:
                self.transition_state -= 1
            else:
                return
        r = self.smooth_transition(sr, tr, self.smoothness, self.transition_state)
        g = self.smooth_transition(sg, tg, self.smoothness, self.transition_state)
        b = self.smooth_transition(sb, tb, self.smoothness, self.transition_state)
        self.current_color = [r, g, b]

    def check_for_click(self, the_event: pg.event.Event):
        return self.hovering and the_event.type == pg.MOUSEBUTTONDOWN


factor = 6
buttons = [([Button([25 * i, 25 * j], [25, 25], [factor * i, factor * j, factor * int((i + j) / 2)],
                    [225 - factor * i, 225 - factor * j, 255 - factor * int((i + j) / 2)], smoothness=30) for i in
             range(18 * 2)])
           for j in range(10 * 2)]
buttons = [button for sub in buttons for button in sub]

if __name__ == '__main__':
    while run:
        pg.display.update()
        for button in buttons:
            button.draw()
        for event in pg.event.get():
            for button in buttons:
                button.check_for_hovering(event)
                if button.check_for_click(event):
                    print("click")
            if event.type == pg.QUIT:
                pg.quit()
                run = False
        clock.tick(FBS)
