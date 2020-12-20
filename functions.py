from BFSClass import BFS
from NODEClass import NODE
from main import *


def createGrid():
    grid = [[NODE(j, i, CELLSIZE) for i in range(width)] for j in range(height)]
    # border
    for i in range(width):
        grid[0][i].setCell(-1, COLOR["BLACK"], True)
        grid[height - 1][i].setCell(-1, COLOR["BLACK"], True)
    for j in range(height):
        grid[j][0].setCell(-1, COLOR["BLACK"], True)
        grid[j][width - 1].setCell(-1, COLOR["BLACK"], True)
    return grid


def getMousePos():
    mouseCol, mouseRow = pygame.mouse.get_pos()
    mouseX, mouseY = mouseCol // CELLSIZE, mouseRow // CELLSIZE
    return mouseY, mouseX


def valid(x, y):
    return 0 < x < width - 1 and 0 < y < height - 1


def drawPath(alg, start, end, walls, grid):
    path = []
    if alg == "BFS":
        path = BFS(start, end, walls, grid).main()

    if len(path) == 0:
        return False
    for node in path:
        node.setCell(4, COLOR["PURPLE"], True)
    initStartEnd(start, end)
    return True


def createPath(start, end):
    path = []
    current = end
    while not current.equal(start):
        current = current.parent
        path.append(current)
    return path


def initStartEnd(start, end):
    start.setCell(1, COLOR["GREEN"], True)
    end.setCell(2, COLOR["RED"], True)
