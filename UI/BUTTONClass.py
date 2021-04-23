from settings import *


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

        if "font" in buttonsInfo[id].keys():
            self.fontSize = buttonsInfo[id]["font"]
        else:
            self.fontSize = 23
        self.fontColor = COLOR[('BLACK')]
        self.italic = True
        self.bold = True

        # functions
        self.highLighted = False
        self.algSet = None

    def draw(self, screen):
        if self.highLighted or self.algSet:
            pygame.draw.rect(screen, self.highLight, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        # font
        font = pygame.font.SysFont("comicsans", self.fontSize, self.bold, self.italic)
        label = font.render(self.msg, True, self.fontColor)
        text_rect = label.get_rect(center=(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.width/2 -20))
        screen.blit(label, text_rect)

    def onButton(self, pos):
        if self.rect.collidepoint(pos[0], pos[1]):
            return True

    def highlightButton(self):
        self.highLighted = True

    def unhighlightButton(self):
        self.highLighted = False

