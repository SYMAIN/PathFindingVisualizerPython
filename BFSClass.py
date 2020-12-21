import functions as f
from GRAPHClass import GRAPH
from main import COLOR, pygame


class BFS(GRAPH):
    def main(self):

        while len(self.qu) != 0:
            node = self.qu.pop(0)
            self.visited[node] = True
            node.setCell(4, COLOR["TURQUOISE"], True)
            f.reDrawGrid(self.grid)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return []
            if node.posEqual(self.end):
                return f.createPath(self.start, self.end)

            for y, x in (-1, 0), (0, -1), (0, 1), (1, 0):
                newPos = (node.y + y, node.x + x)
                if f.valid(newPos[1], newPos[0]):
                    child = self.grid[newPos[0]][newPos[1]]

                    if self.validPos(child):
                        self.qu.append(child)
                        child.parent = node
                        child.setCell(5, COLOR["ORANGE"], True)

            f.reDrawGrid(self.grid)
            node.setCell(6, COLOR["YELLOW"], True)
            self.clock.tick(120)
