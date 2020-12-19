class BFS:
    def __init__(self, start, end, walls):
        self.start = start
        self.end = end
        self.walls = walls

    def main(self):
        qu = set(self.start)
        visited = {}

        while len(qu) != 0:
            node = qu.pop()
            visited[node] = True

            for y, x in (0, 1), (1, 0), (0, -1), (-1, 0):
                child = (node[0] + y, node[1] + x)
                if not visited[child] and child not in self.walls:
                    qu.add(child)
