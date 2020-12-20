import pygame

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

class NODE:
    def __init__(self, y, x, size):
        self.x = x  # position/ idx of cell in grid
        self.y = y  # position/ idx of cell in grid
        self.col = x * size  # position of cell on display
        self.row = y * size  # position of cell on display
        self.size = size
        self.color = -1
        self.state = 0  # 0=space, 1=start, 2=end, 3=wall, 4= border

        self.fill = 0  # cell color fill or empty

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

    def moveCell(self, cell):
        cell.col, self.col = self.col, cell.col
        cell.row, self.row = self.row, cell.row

    def setToWall(self):
        self.state = 3
        self.color = COLOR["DARKGREY"]
        self.fill = True

    def resetCell(self):
        self.state = 0
        self.color = -1
        self.fill = False
