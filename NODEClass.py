import pygame


class NODE:
    def __init__(self, y, x, size):
        self.x = x  # position/ idx of cell in grid
        self.y = y  # position/ idx of cell in grid
        self.col = x * size  # position of cell on display
        self.row = y * size  # position of cell on display
        self.size = size
        self.color = -1
        self.state = 0  # 0=space, 1=start, 2=end, 3=wall

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
