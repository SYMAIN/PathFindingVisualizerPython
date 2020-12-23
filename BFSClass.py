import functions as f
from GRAPHClass import GRAPH
from main import COLOR, pygame


class BFS(GRAPH):
    def main(self):

        while len(self.qu) != 0:
            node = self.qu.pop(0)
            self.visited[node] = True
            node.setNode()
            f.reDrawGrid(self.grid)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return []
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

            f.reDrawGrid(self.grid)
            node.setVisted()
            self.clockTick()
