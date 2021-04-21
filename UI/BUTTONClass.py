from main import pygame, COLOR, width, height


class button:
    def __init__(self, col, row, l, w, color, highLight, msg='BFS', id='BFS'):
        self.col = col
        self.row = row
        self.l = l
        self.w = w
        self.rect = pygame.Rect(self.col, self.row, self.w, self.l)

        self.highLight = highLight
        self.color = color
        self.msg = msg  # text
        self.id = id  # the purpose of the button

        self.fontSize = 23
        self.fontColor = COLOR[('BLACK')]
        self.italic = True
        self.bold = True

        # functions
        self.highLighted = False
        self.algSet = False

    def draw(self, screen):
        if self.highLighted or self.algSet:
            pygame.draw.rect(screen, self.highLight, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        # font
        font = pygame.font.SysFont("comicsans", self.fontSize, self.bold, self.italic)
        label = font.render(self.msg, True, self.fontColor)
        screen.blit(label, (self.rect.x + width / 2, self.rect.y + height / 2 - 5))

    def onButton(self, pos):
        if self.rect.collidepoint(pos[0], pos[1]):
            return True

    def highlightButton(self):
        self.highLighted = True

    def unhighlightButton(self):
        self.highLighted = False

