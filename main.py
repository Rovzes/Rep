import os
import sys

import pygame
import requests


def createMap(x, y, z, l):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={x},{y}&z={z}&l={l}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return pygame.image.load("map.png")


x, y = 60, 60
size = 5
mapImage = createMap(x, y, size, "map")

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(mapImage, (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    screen.fill(pygame.Color("black"))
    screen.blit(mapImage, (0, 0))
    pygame.display.flip()
pygame.quit()

os.remove("map.png")
