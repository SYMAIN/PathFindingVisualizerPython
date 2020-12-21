import math

import functions as f
from GRAPHClass import GRAPH
from main import COLOR, pygame

inf = float("inf")


class Astar(GRAPH):
    def main(self):
        nodesValue = {}
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                nodesValue[(i, j)] = [inf, inf, 0]
        # gVal = 0, hVal = 1, fVal = 2
        nodesValue[self.start.y, self.start.x][0] = 0
        nodesValue[self.start.y, self.start.x][1] = self.calcHeur(self.start, self.end)
        nodesValue[self.start.y, self.start.x][2] = nodesValue[self.start.y, self.start.x][0] + \
                                                    nodesValue[self.start.y, self.start.x][1]

        while len(self.qu) != 0:
            node = self.lowestCost(nodesValue)
            self.visited[node] = True
            node.setCell(4, COLOR["TURQUOISE"], True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return []
            if node.posEqual(self.end):
                return f.createPath(self.start, self.end)

            for y, x in (-1, 0), (0, -1), (0, 1), (1, 0):
                newPos = (node.y + y, node.x + x)
                if f.valid(newPos[1], newPos[0]):
                    child = self.grid[newPos[0]][newPos[1]]
                    tentative_gScore = nodesValue[node.y, node.x][0] + 1
                    if tentative_gScore < nodesValue[child.y, child.x][0] and child not in self.visited and child not in self.walls:
                        child.parent = node
                        child.setCell(5, COLOR["ORANGE"], True)
                        nodesValue[child.y, child.x][0] = tentative_gScore
                        nodesValue[child.y, child.x][1] = self.calcHeur(child, self.end)
                        nodesValue[child.y, child.x][2] = nodesValue[child.y, child.x][0] + \
                                                          nodesValue[child.y, child.x][1]
                        if child not in self.qu:
                            self.qu.append(child)

            f.reDrawGrid(self.grid)
            node.setCell(6, COLOR["YELLOW"], True)
            self.clock.tick(120)

    def lowestCost(self, nodes):
        node = self.qu[0]
        for item in self.qu:
            if nodes[item.y, item.x][2] < nodes[node.y, node.x][2]:
                node = item
        self.qu.remove(node)
        return node

    def calcHeur(self, current, end):
        a = abs(current.x - end.x)
        b = abs(current.y - end.y)
        return math.sqrt(a ** 2 + b ** 2)
