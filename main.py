import pygame

from pathFinding_2.NODEClass import NODE

"""
col and row are mostly for position on display
x and y are mostly for idx of the grid list or for cell position
"""
pygame.init()

WIDTH, HEIGHT = (800, 800)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
height = 50
panelSize = 10
width = 50 - panelSize
CELLSIZE = WIDTH // height
delay = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TURQUOISE = (0, 183, 255)
ORANGE = (255, 102, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (170, 0, 204)


class DISPLAY:
    def __init__(self):
        self.grid = createGrid()

        self.start = self.grid[20][20]
        self.start.setCell(1, RED, True)
        self.end = self.grid[20][21]
        self.end.setCell(2, GREEN, True)

    def run(self):  # main loop
        run = True
        clock = pygame.time.Clock()

        # events
        startEndDrag = False
        startEndPos = (0, 0)

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:  # mouse button pressed
                    mouseY, mouseX = getMousePos()
                    if vaild(mouseX, mouseY) and event.button == 1:
                        state = self.grid[mouseY][mouseX].state
                        if state == 1 or state == 2:  # current state is the start or end
                            startEndDrag = True
                            startEndPos = (mouseY, mouseX)
                            print("clicked")
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        startEndDrag = False

            # update
            if startEndDrag:
                mouseY, mouseX = getMousePos()
                if vaild(mouseX, mouseY) and startEndPos != (mouseY, mouseX):
                    self.grid[startEndPos[0]][startEndPos[1]].moveCell(self.grid[mouseY][mouseX])
                    startEndPos = (mouseY, mouseX)
            self.draw()
            pygame.display.update()
            clock.tick(120)
        pygame.display.quit()

    def draw(self):  # draw all graphic
        screen.fill(GREY)  # set background color
        # draw grid
        for i in self.grid:
            for cell in i:
                cell.draw(screen)


def createGrid():
    grid = [[NODE(j, i, CELLSIZE) for i in range(width)] for j in range(height)]
    # border
    for i in range(width):
        grid[0][i].setCell(3, BLACK, True)
        grid[height - 1][i].setCell(3, BLACK, True)
    for j in range(height):
        grid[j][0].setCell(3, BLACK, True)
        grid[j][width - 1].setCell(3, BLACK, True)
    return grid


def getMousePos():
    mouseCol, mouseRow = pygame.mouse.get_pos()
    mouseX, mouseY = mouseCol // CELLSIZE, mouseRow // CELLSIZE
    return mouseY, mouseX


def vaild(x, y):
    return 0 < x < width - 1 and 0 < y < height - 1


if __name__ == '__main__':
    DISPLAY().run()


"""
fix dragging start/end to any point in grid
add/delete walls feature
implement A-star,bfs,dfs,ect.
add side interface and functionally buttons
"""