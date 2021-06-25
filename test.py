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

pygame.init()
tail_length = 500
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
FBS = 90
clock.tick(FBS)
run = True
j = 0

places = [(100, 100), ]
for _ in range(100):
    places.append((random.randint(100, 200), random.randint(100, 200)))
places.append((100, 100))
length = 10
distances = []
color = (225, 255, 255)
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
        for k in range(-10, 11, 10):
            window.set_at([i + k for i in points[j]],
                          (int((degree * 225) / tail_length), int((degree * 100) / tail_length),
                           int((degree * 100) / tail_length),))
    pygame.display.flip()
    clock.tick(FBS)

pygame.quit()
exit()
