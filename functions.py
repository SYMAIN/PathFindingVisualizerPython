import pygame

from BFSClass import BFS
from NODEClass import NODE

COLOR = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "GREY": (150, 150, 150),
    "GREEN": (0, 255, 0),
    "RED": (255, 0, 0),
    "TURQUOISE": (0, 183, 255),
    "ORANGE": (255, 102, 0),
    "YELLOW": (255, 255, 0),
    "BLUE": (0, 0, 255),
    "PURPLE": (170, 0, 204),
    "DARKGREY": (50, 50, 50)
}
pygame.init()
WIDTH, HEIGHT = (800, 800)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
height = 50
panelSize = 10
width = 50 - panelSize
CELLSIZE = WIDTH // height
delay = 0


def createGrid():
    grid = [[NODE(j, i, CELLSIZE) for i in range(width)] for j in range(height)]
    # border
    for i in range(width):
        grid[0][i].setCell(-1, COLOR["BLACK"], True)
        grid[height - 1][i].setCell(-1, COLOR["BLACK"], True)
    for j in range(height):
        grid[j][0].setCell(-1, COLOR["BLACK"], True)
        grid[j][width - 1].setCell(-1, COLOR["BLACK"], True)
    return grid


def getMousePos():
    mouseCol, mouseRow = pygame.mouse.get_pos()
    mouseX, mouseY = mouseCol // CELLSIZE, mouseRow // CELLSIZE
    return mouseY, mouseX


def valid(x, y):
    return 0 < x < width - 1 and 0 < y < height - 1


def drawPath(alg, start, end, walls, grid):
    if alg == "BFS":
        BFS(start, end, walls, grid).main()
