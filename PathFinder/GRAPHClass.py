import UIfunc as f
import PathFinder.PathFindingFunc as pf
from  settings import *


class GRAPH:
    def __init__(self, start, end, walls, grid, delay):
        self.start = start
        self.end = end
        self.walls = walls
        self.grid = grid
        self.delay = delay

        self.qu = [self.start]
        self.visited = {}
        self.clock = pygame.time.Clock()

    def validPos(self, child):
        return child not in self.visited and child not in self.qu and child not in self.walls

    def clockTick(self):
        self.clock.tick(60)

    def drawScreen(self):
        f.reDrawScreen(self.grid)
        pf.delayTimer(self.delay)

    def changeSpeed(self):
        for s in sliders:
            if s.hit:
                s.move()
                if s.name == "speed":
                    # change speed
                    self.delay = 1 - s.val

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for s in sliders:
                    if s.button_rect.collidepoint(pos):
                        s.hit = True
            if event.type == pygame.MOUSEBUTTONUP:
                for s in sliders:
                    s.hit = False
        self.changeSpeed()
        return True
