import math

import functions as f
from main import pygame, COLOR


class GRAPH:
    def __init__(self, start, end, walls, grid):
        self.start = start
        self.end = end
        self.walls = walls
        self.grid = grid

        self.qu = [self.start]
        self.visited = {}
        self.clock = pygame.time.Clock()

    def validPos(self, child):
        return child not in self.visited and child not in self.qu and child not in self.walls