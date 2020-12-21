from main import pygame,COLOR
import functions as f


class GRAPH:
    def __init__(self, start, end, walls, grid):
        self.start = start
        self.end = end
        self.walls = walls
        self.grid = grid

        self.qu = [self.start]
        self.visited = {}
        self.clock = pygame.time.Clock()

    def findNeighbors(self, node):
        for y, x in (-1, 0), (0, -1), (0, 1), (1, 0):
            newPos = (node.y + y, node.x + x)
            if f.valid(newPos[1], newPos[0]):
                child = self.grid[newPos[0]][newPos[1]]

                if child not in self.visited and child not in self.walls and child not in self.qu:
                    self.qu.append(child)
                    child.parent = node
                    child.setCell(5, COLOR["ORANGE"], True)
