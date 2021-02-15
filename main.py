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
    "DARKGREY": (50, 50, 50),
    "TRANS" : (1, 1, 1)

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
        buttons = f.algButtons()

        sliders = []
        sliders.append(f.createSlider("speed", 1, 1, 0.5, 655, 175))

        while run:
            # update events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                # highlight button when hovering over
                for val in buttons.values():
                    if val.id != self.alg:
                        if val.onButton(pygame.mouse.get_pos()):
                            val.highlightButton()
                        else:
                            val.unhighlightButton()

                if event.type == pygame.MOUSEBUTTONDOWN:  # mouse button pressed
                    mouseY, mouseX = f.getMousePos()
                    # left click down
                    if event.button == 1:
                        if f.valid(mouseX, mouseY):
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
                        clicked = False
                        for val in buttons.values():
                            if val.onButton(pygame.mouse.get_pos()):
                                clicked = True
                        if clicked:
                            for val in buttons.values():
                                if val.set:
                                    if val.onButton(pygame.mouse.get_pos()) and val.id == self.alg:
                                        val.set = True
                                    else:
                                        val.set = False
                                elif not val.set:
                                    if val.onButton(pygame.mouse.get_pos()) and val.id != self.alg:
                                        val.set = True
                                        self.alg = val.id
                                    else:
                                        val.set = False
                        pos = pygame.mouse.get_pos()
                        for s in sliders:
                            if s.button_rect.collidepoint(pos):
                                s.hit = True

                    # right click down
                    if event.button == 3:
                        mouseY, mouseX = f.getMousePos()
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
                        f.clearALL(self.grid, self.walls)

                    # space key click -> start alg
                    if event.key == pygame.K_SPACE:
                        a = f.drawPath(self.alg, self.start, self.end, self.walls, self.grid, delay, buttons, sliders)
                        if not a:
                            run = False

                    # x key click -> clear the paths created
                    if event.key == pygame.K_x:
                        f.clearPath(self.grid)

            # move start/end
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

            # add walls
            if wallDrag:
                mouseY, mouseX = f.getMousePos()
                if f.valid(mouseX, mouseY):
                    current = self.grid[mouseY][mouseX]
                    if current.state == 0 and current not in self.walls:
                        current.setWall()
                        self.walls.append(current)

            # remove walls
            if removeDrag:
                mouseY, mouseX = f.getMousePos()
                if f.valid(mouseX, mouseY):
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
                        print("speed:",s.val)
                        delay = 1 - s.val

            # draw
            f.reDrawScreen(self.grid, buttons,sliders)

            clock.tick(120)
        pygame.display.quit()


if __name__ == '__main__':
    DISPLAY().run()
