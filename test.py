import random
import pygame

# import os, sys
#
#
# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)
WINDOW_LENGTH = 1000
WINDOW_HIGHT = 600
pygame.init()
tail_length = 300
num_of_lines = 10
window = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HIGHT))
clock = pygame.time.Clock()
FBS = 90
clock.tick(FBS)
run = True
j = 0

# Set the starting possetion of the lines.
start = (WINDOW_LENGTH // 2, WINDOW_HIGHT // 2)
places = [start, ]
for _ in range(20):
    places.append((random.randint(0, 600), random.randint(0, 600)))
places.append(start)
length = 10
distances = []
color = (25, 200, 25)
points = []


def gray_shade(color_degree):
    return (color_degree,) * 3


for i in range(len(places) - 1):
    delta_x = abs(places[i][0] - places[i + 1][0])
    delta_y = abs(places[i][1] - places[i + 1][1])
    distance = max(delta_x, delta_y)
    distances.append(distance)

for i in range(sum(distances)):
    for j in range(len(distances)):
        start = sum(distances[0:j])
        finish = sum(distances[0:j + 1])
        if i in range(start, finish):
            x, y = places[j]
            x_d_factor = (places[j][0] - places[j + 1][0]) / distances[j]
            y_d_factor = (places[j][1] - places[j + 1][1]) / distances[j]
            factor = i - start
            x -= x_d_factor * factor
            y -= y_d_factor * factor
            point = (int(x), int(y))
            points.append(point)
i = 0
while run:
    i = (i + 2) % len(points)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(0)
    for degree, j in enumerate(range(i - tail_length, i)):
        for k in range(num_of_lines * -1, num_of_lines , 2):
            window.set_at([i + k for i in points[j]],
                          (int((degree * color[0]) / tail_length), int((degree * color[1]) / tail_length),
                           int((degree * color[2]) / tail_length),))
    pygame.display.flip()
    clock.tick(FBS)

pygame.quit()
exit()
