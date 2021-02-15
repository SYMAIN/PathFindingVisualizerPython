from ASTARClass import Astar
from BFSClass import BFS
from BUTTONClass import button
from NODEClass import NODE
from SLIDERClass import slider
from main import *
import time


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


def drawPath(alg, start, end, walls, grid, delay, buttons,sliders):
    path = []
    clearPath(grid)
    if alg == "BFS":
        path = BFS(start, end, walls, grid, delay, buttons,sliders).main()
    elif alg == "ASTAR":
        path = Astar(start, end, walls, grid, delay, buttons,sliders).main()

    initStartEnd(start, end)
    if path == []:
        print("Path not Found")
        return True
    if path is None:
        return False
    for node in path:
        node.setCell(4, COLOR["PURPLE"], True)
    print("Path Found")
    print(alg, len(path))
    return True


def createPath(start, end):
    path = []
    current = end
    while not current.posEqual(start):
        path.append(current)
        current = current.parent
    path.pop(0)
    return path


def initStartEnd(start, end):
    start.setStart()
    end.setEnd()


def reDrawScreen(grid, buttons,sliders):
    screen.fill(COLOR["GREY"])  # set background color
    # draw grid
    for i in grid:
        for cell in i:
            cell.draw(screen)
    for bnt in buttons.values():
        bnt.draw(screen)

    for s in sliders:
        s.draw()
    pygame.display.update()


def clearPath(grid):
    for i in grid:
        for j in i:
            if j.state == 4 or j.state == 5 or j.state == 6:
                j.resetCell()


def clearALL(grid, walls):
    for i in grid:
        for j in i:
            if j.state != 1 and j.state != 2 and j.state != -1:
                if j.state == 3:
                    walls.remove(j)
                j.resetCell()


def createButton(col, row, l, w, color, hl, msg, id):
    return button(col, row, l, w, color, hl, msg, id)

def algButtons():
    buttons = {}
    bfs = createButton(654, 24, 50, 100, COLOR["WHITE"], COLOR["TURQUOISE"], "BFS", "BFS")
    astar = createButton(654, 104, 50, 100, COLOR["WHITE"], COLOR["TURQUOISE"], "ASTAR", "AStar")

    # init default setting
    bfs.set = True

    buttons[bfs.id] = bfs
    buttons[astar.id] = astar
    return buttons

def createSlider(name,val,maxi,mini,xpos,ypos):
    return slider(name,val,maxi,mini,xpos,ypos)

def delayTimer(sec):
    max = sec
    start = time.time()
    while True:
        ### Do other stuff, it won't be blocked
        time.sleep(sec)

        ### This will be updated every loop
        remaining = max + start - time.time()
        print(remaining)

        ### Countdown finished, ending loop
        if remaining <= 0:
            break