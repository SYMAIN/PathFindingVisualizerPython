import pygame

import functions as f

"""
col and row are mostly for position on display
x and y are mostly for idx of the grid list or for cell position
"""

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


class DISPLAY:
    def __init__(self):
        self.walls = []
        self.grid = f.createGrid()

        self.start = self.grid[20][20]  # random position on the grid
        self.end = self.grid[20][21]  # random position on the grid
        f.initStartEnd(self.start, self.end)

    def run(self):  # main loop
        run = True
        clock = pygame.time.Clock()

        # events
        startEnd = (False, -1)  # drag, id--> 0=start,1=end
        startEndPos = (0, 0)

        wallDrag = False
        removeDrag = False

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:  # mouse button pressed
                    mouseY, mouseX = f.getMousePos()
                    if f.valid(mouseX, mouseY) and event.button == 1:
                        state = self.grid[mouseY][mouseX].state
                        if state == 1:  # current state is the start
                            startEnd = (True, 0)
                            startEndPos = (mouseY, mouseX)
                        elif state == 2:  # current state is the end
                            startEnd = (True, 1)
                            startEndPos = (mouseY, mouseX)
                        elif state == 0 or state == 3:
                            wallDrag = True
                    if event.button == 3:
                        mouseY, mouseX = f.getMousePos()
                        current = self.grid[mouseY][mouseX]
                        if current.state == 3 or current.state == 0:
                            removeDrag = True

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        startEnd = (False, -1)
                        wallDrag = False
                    if event.button == 3:
                        removeDrag = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        self.clearALL()
                    if event.key == pygame.K_SPACE:
                        if not f.drawPath("BFS", self.start, self.end, self.walls, self.grid):
                            run = False

            # update
            if startEnd[0]:
                mouseY, mouseX = f.getMousePos()  # new position
                if f.valid(mouseX, mouseY) and startEndPos != (mouseY, mouseX):
                    new = self.grid[mouseY][mouseX]
                    if new.state == 0:
                        SE = self.grid[startEndPos[0]][startEndPos[1]]
                        new.setCell(SE.state, SE.color, SE.fill)
                        SE.resetCell()
                        startEndPos = (mouseY, mouseX)
                        if startEnd[1] == 0:
                            self.start = new
                        elif startEnd[1] == 1:
                            self.end = new

            if wallDrag:
                mouseY, mouseX = f.getMousePos()
                if f.valid(mouseX, mouseY):
                    current = self.grid[mouseY][mouseX]
                    if current.state == 0 and current not in self.walls:
                        current.setCell(3, COLOR["DARKGREY"], True)
                        self.walls.append(current)

            if removeDrag:
                mouseY, mouseX = f.getMousePos()
                if f.valid(mouseX, mouseY):
                    current = self.grid[mouseY][mouseX]
                    if current.state == 3:
                        current.setCell(0, -1, False)
                        self.walls.remove(current)

            self.draw(screen)
            pygame.display.update()
            clock.tick(120)
        pygame.display.quit()

    def draw(self, screen):  # draw all graphic
        screen.fill(COLOR["GREY"])  # set background color
        # draw grid
        for i in self.grid:
            for cell in i:
                cell.draw(screen)

    def clearALL(self):
        for i in self.grid:
            for j in i:
                if j.state != 1 and j.state != 2 and j.state != -1:
                    j.resetCell()


if __name__ == '__main__':
    DISPLAY().run()
