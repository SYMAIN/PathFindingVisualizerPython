import functions as f

from main import COLOR, screen, pygame


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
            node = qu.pop(0)
            visited[node] = True
            node.setCell(4, COLOR["TURQUOISE"], True)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return []
            if node.equal(self.end):
                return f.createPath(self.start, self.end)

            for y, x in (0, 1), (1, 0), (0, -1), (-1, 0):
                newPos = (node.y + y, node.x + x)
                if f.valid(newPos[1], newPos[0]):
                    child = self.grid[newPos[0]][newPos[1]]

                    if child not in visited and child not in self.walls and child not in qu:
                        qu.append(child)
                        child.parent = node
                        child.setCell(5, COLOR["ORANGE"], True)
                        self.draw()

            node.setCell(6, COLOR["YELLOW"], True)
            clock.tick(120)

    def draw(self):
        screen.fill(COLOR["GREY"])  # set background color
        # draw grid
        for i in self.grid:
            for cell in i:
                cell.draw(screen)
        pygame.display.update()
