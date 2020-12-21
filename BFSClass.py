import functions as f

from main import COLOR, pygame
from graph import GRAPH


class BFS(GRAPH):
    def main(self):

        while len(self.qu) != 0:
            node = self.qu.pop(0)
            self.visited[node] = True
            node.setCell(4, COLOR["TURQUOISE"], True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return []
            if node.posEqual(self.end):
                return f.createPath(self.start, self.end)

            self.findNeighbors(node)

            f.reDrawGrid(self.grid)
            node.setCell(6, COLOR["YELLOW"], True)
            self.clock.tick(120)
