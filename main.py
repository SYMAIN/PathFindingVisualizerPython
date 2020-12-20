from functions import *

"""
col and row are mostly for position on display
x and y are mostly for idx of the grid list or for cell position
"""


class DISPLAY:
    def __init__(self):
        self.walls = []
        self.grid = createGrid()

        self.start = self.grid[20][20]  # random position on the grid
        self.start.setCell(1, COLOR["RED"], True)
        self.end = self.grid[20][21]  # random position on the grid
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
                    if valid(mouseX, mouseY) and event.button == 1:
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
                    if event.key == pygame.K_SPACE:
                        drawPath("BFS", self.start, self.end, self.walls, self.grid)

            # update
            if startEndDrag:
                mouseY, mouseX = getMousePos()  # new position
                if valid(mouseX, mouseY) and startEndPos != (mouseY, mouseX):
                    new = self.grid[mouseY][mouseX]
                    if new.state != 3 and new.state != 2 and new.state != 1:
                        startEnd = self.grid[startEndPos[0]][startEndPos[1]]
                        new.setCell(startEnd.state, startEnd.color, startEnd.fill)
                        startEnd.resetCell()
                        startEndPos = (mouseY, mouseX)

            if wallDrag:
                mouseY, mouseX = getMousePos()
                if valid(mouseX, mouseY):
                    current = self.grid[mouseY][mouseX]
                    if current.state != 1 and current.state != 2:
                        current.setCell(3, COLOR["DARKGREY"], True)
                        self.walls.append(current)

            if removeDrag:
                mouseY, mouseX = getMousePos()
                if valid(mouseX, mouseY):
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
                if j.state == 3:
                    j.resetCell()


if __name__ == '__main__':
    DISPLAY().run()
