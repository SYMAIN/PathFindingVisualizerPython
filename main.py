from  settings import *

import UIfunc as uf
import PathFinder.PathFindingFunc as pf

"""
col and row are mostly for position on display
x and y are mostly for idx of the grid list or for cell position
"""

class DISPLAY:
    def __init__(self):
        self.walls = []
        self.grid = uf.createGrid()

        self.start = self.grid[20][20]  # random position on the grid
        self.end = self.grid[20][21]  # random position on the grid

        # init position
        pf.initStartEnd(self.start, self.end)

        self.alg = 'BFS'  # default

    def run(self):  # main loop
        run = True
        clock = pygame.time.Clock()
        delay = 0

        # events
        startEnd = (False, -1)  # drag, id--> 0=start,1=end
        startEndPos = (0, 0)

        wallDrag = False
        removeDrag = False

        # init the algorithm selection buttons
        uf.algButtons()

        # init sliders
        uf.sliderUI()

        while run:
            # update events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                uf.buttonHover()

                if event.type == pygame.MOUSEBUTTONDOWN:  # mouse button pressed
                    mouseY, mouseX = uf.getMousePos()
                    # left click down
                    if event.button == 1:
                        if uf.valid(mouseX, mouseY):
                            state = self.grid[mouseY][mouseX].state
                            if state == 1:  # current state is the start
                                startEnd = (True, 0)
                                startEndPos = (mouseY, mouseX)
                            elif state == 2:  # current state is the end
                                startEnd = (True, 1)
                                startEndPos = (mouseY, mouseX)
                            elif state == 0 or state == 3:
                                wallDrag = True

                        # check if button is clicked
                        self.alg = uf.buttonClicked(self.alg)

                        uf.sliderClicked()

                    # right click down
                    if event.button == 3:
                        mouseY, mouseX = uf.getMousePos()
                        current = self.grid[mouseY][mouseX]
                        if current.state == 3 or current.state == 0:
                            removeDrag = True

                if event.type == pygame.MOUSEBUTTONUP:
                    # left click up
                    if event.button == 1:
                        startEnd = (False, -1)
                        wallDrag = False

                    # right click up
                    if event.button == 3:
                        removeDrag = False

                    # unclick sliders
                    for s in sliders:
                        s.hit = False

                if event.type == pygame.KEYDOWN:
                    # z key click -> clear all walls/paths
                    if event.key == pygame.K_z:
                        uf.clearALL(self.grid, self.walls)

                    # space key click -> start alg
                    if event.key == pygame.K_SPACE:
                        a = pf.drawPath(self.alg, self.start, self.end, self.walls, self.grid, delay)
                        if not a:
                            run = False

                    # x key click -> clear the paths created
                    if event.key == pygame.K_x:
                        uf.clearPath(self.grid)

            # move start/end
            if startEnd[0]:
                mouseY, mouseX = uf.getMousePos()  # new position
                if uf.valid(mouseX, mouseY) and startEndPos != (mouseY, mouseX):
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

            # add walls
            if wallDrag:
                mouseY, mouseX = uf.getMousePos()
                if uf.valid(mouseX, mouseY):
                    current = self.grid[mouseY][mouseX]
                    if current.state == 0 and current not in self.walls:
                        current.setWall()
                        self.walls.append(current)

            # remove walls
            if removeDrag:
                mouseY, mouseX = uf.getMousePos()
                if uf.valid(mouseX, mouseY):
                    current = self.grid[mouseY][mouseX]
                    if current.state == 3:
                        current.setCell(0, -1, False)
                        self.walls.remove(current)

            # move sliders
            for s in sliders:
                if s.hit:
                    s.move()
                    if s.name == "speed":
                        # change speed
                        delay = 1 - s.val

            # draw
            uf.reDrawScreen(self.grid)

            clock.tick(120)
        pygame.display.quit()


if __name__ == '__main__':
    DISPLAY().run()
