import pygame

from NODEClass import NODE, COLOR

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


class DISPLAY:
    def __init__(self):
        self.walls = []
        self.grid = createGrid()

        self.start = self.grid[20][20]
        self.start.setCell(1, COLOR["RED"], True)
        self.end = self.grid[20][21]
        self.end.setCell(2, COLOR["GREEN"], True)

    def run(self):  # main loop
        run = True
        clock = pygame.time.Clock()

        # events
        startEndDrag = False
        startEndPos = (0, 0)

        wallDrag = False
        removeDrag = False

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
                        elif state == 0 or state == 3:
                            wallDrag = True
                    if event.button == 3:
                        mouseY, mouseX = getMousePos()
                        current = self.grid[mouseY][mouseX]
                        if current.state == 3 or current.state == 0:
                            removeDrag = True

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        startEndDrag = False
                        wallDrag = False
                    if event.button == 3:
                        removeDrag = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        self.clearALL()

            # update
            if startEndDrag:
                mouseY, mouseX = getMousePos()
                if vaild(mouseX, mouseY) and startEndPos != (mouseY, mouseX):
                    self.grid[startEndPos[0]][startEndPos[1]].moveCell(self.grid[mouseY][mouseX])
                    self.grid[startEndPos[0]][startEndPos[1]], self.grid[mouseY][mouseX] = self.grid[mouseY][mouseX], \
                                                                                           self.grid[startEndPos[0]][
                                                                                               startEndPos[1]]

                    startEndPos = (mouseY, mouseX)

            if wallDrag:
                mouseY, mouseX = getMousePos()
                if vaild(mouseX, mouseY):
                    current = self.grid[mouseY][mouseX]
                    if current.state != 1 and current.state != 2:
                        current.setToWall()
                        self.walls.append(current)

            if removeDrag:
                mouseY, mouseX = getMousePos()
                if vaild(mouseX, mouseY):
                    current = self.grid[mouseY][mouseX]
                    if current.state == 3:
                        current.setCell(0, -1, False)
                        self.walls.remove(current)
            self.draw()
            pygame.display.update()
            clock.tick(120)
        pygame.display.quit()

    def draw(self):  # draw all graphic
        screen.fill(COLOR["GREY"])  # set background color
        # draw grid
        for i in self.grid:
            for cell in i:
                cell.draw(screen)

    def clearALL(self):
        for i in self.grid:
            for j in i:
                if j.state == 3:
                    j.resetCell()


def createGrid():
    grid = [[NODE(j, i, CELLSIZE) for i in range(width)] for j in range(height)]
    # border
    for i in range(width):
        grid[0][i].setCell(4, COLOR["BLACK"], True)
        grid[height - 1][i].setCell(4, COLOR["BLACK"], True)
    for j in range(height):
        grid[j][0].setCell(4, COLOR["BLACK"], True)
        grid[j][width - 1].setCell(4, COLOR["BLACK"], True)
    return grid


def getMousePos():
    mouseCol, mouseRow = pygame.mouse.get_pos()
    mouseX, mouseY = mouseCol // CELLSIZE, mouseRow // CELLSIZE
    return mouseY, mouseX


def vaild(x, y):
    return 0 < x < width - 1 and 0 < y < height - 1


if __name__ == '__main__':
    DISPLAY().run()
