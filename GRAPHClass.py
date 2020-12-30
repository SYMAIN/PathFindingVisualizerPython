from main import pygame
import functions as f


class GRAPH:
    def __init__(self, start, end, walls, grid, buttons):
        self.start = start
        self.end = end
        self.walls = walls
        self.grid = grid
        self.buttons = buttons

        self.qu = [self.start]
        self.visited = {}
        self.clock = pygame.time.Clock()

    def validPos(self, child):
        return child not in self.visited and child not in self.qu and child not in self.walls

    def clockTick(self):
        self.clock.tick(40)

    def drawScreen(self):
        f.reDrawScreen(self.grid, self.buttons)
