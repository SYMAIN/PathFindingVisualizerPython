from main import pygame, COLOR


class button:
    def __init__(self, col, row, l, w, color, msg):
        self.col = col
        self.row = row
        self.l = l
        self.w = w

        self.color = color
        self.msg = msg

        self.fontSize = 36
        self.fontColor = COLOR[('BLACK')]
        self.italic = False
        self.bold = False

    def draw(self, screen):
        rect = pygame.Rect(self.col, self.row, self.w, self.l)
        pygame.draw.rect(screen, self.color, rect)
        pygame.display.update()


