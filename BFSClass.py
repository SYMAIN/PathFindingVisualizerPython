from functions import *


class BFS:
    def __init__(self, start, end, walls, grid):
        self.start = start
        self.end = end
        self.walls = walls
        self.grid = grid

    def main(self):
        qu = [self.start]
        visited = {}
        clock = pygame.time.Clock()

        while len(qu) != 0:
            node = qu.pop()
            visited[node] = True
            node.setCell(4, COLOR["TURQUOISE"], True)
            self.draw()

            if node == self.end:
                return

            for y, x in (0, 1), (1, 0), (0, -1), (-1, 0):
                newPos = (node.y + y, node.x + x)
                if valid(newPos[1], newPos[0]):
                    child = self.grid[newPos[0]][newPos[1]]

                    if child not in visited and child not in self.walls:
                        qu.append(child)
                        child.parent = node
                        child.setCell(5, COLOR["Orange"], True)
                        self.draw()

            node.setCell(6, COLOR["YELLOW"], True)
            clock.tick(120)
            self.draw()

    def draw(self):
        screen.fill(COLOR["GREY"])  # set background color
        # draw grid
        for i in self.grid:
            for cell in i:
                cell.draw(screen)
        pygame.display.update()
