import pygame
from main import COLOR


class NODE:
    def __init__(self, y, x, size):
        self.x = x  # position/ idx of cell in grid
        self.y = y  # position/ idx of cell in grid
        self.col = x * size  # position of cell on display
        self.row = y * size  # position of cell on display
        self.size = size

        self.color = -1
        self.state = 0  # -1=border, 0=space, 1=start, 2=end, 3=wall, 4=node, 5=neighbors,6=visited
        self.fill = 0  # cell color fill or empty

        self.parent = -1

    def draw(self, screen):
        rect = pygame.Rect(self.col, self.row, self.size, self.size)
        if self.fill:
            pygame.draw.rect(screen, self.color, rect)
        else:
            pygame.draw.rect(screen, self.color, rect, 1)

    def setCell(self, state, color, fill):
        self.state = state
        self.color = color
        self.fill = fill

    def resetCell(self):
        self.state = 0
        self.color = -1
        self.fill = False

    def posEqual(self, node):
        return self.x == node.x and self.y == node.y

    def setWall(self):
        self.setCell(3, COLOR["DARKGREY"], True)

    def setNode(self):
        self.setCell(4, COLOR["TURQUOISE"], True)

    def setNeighbor(self):
        self.setCell(5, COLOR["ORANGE"], True)

    def setVisted(self):
        self.setCell(6, COLOR["YELLOW"], True)

    def setStart(self):
        self.setCell(1, COLOR["GREEN"], True)

    def setEnd(self):
        self.setCell(2, COLOR["RED"], True)
