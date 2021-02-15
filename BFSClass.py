import functions as f
from GRAPHClass import GRAPH
from main import pygame


class BFS(GRAPH):

    def __init__(self, start, end, walls, grid, delay, buttons,sliders):
        super().__init__(start, end, walls, grid, delay, buttons,sliders)

    def main(self):

        while len(self.qu) != 0:
            node = self.getNode()
            self.visited[node] = True

            if (not self.checkEvents()):
                return None

            if node.posEqual(self.end):
                return f.createPath(self.start, self.end)

            for y, x in (-1, 0), (0, -1), (0, 1), (1, 0):
                newY, newX = node.y + y, node.x + x
                if f.valid(newX, newY):
                    child = self.grid[newY][newX]

                    if self.validPos(child):
                        self.qu.append(child)
                        child.parent = node
                        child.setNeighbor()

            self.drawScreen()
            node.setVisted()
            self.clockTick()
    def getNode(self):
        node = self.qu.pop(0)
        node.setNode()
        return node