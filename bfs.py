from pyMaze import maze, agent, COLOR

#BFS Function
def BFS(m):
    start = (m.rows, m.rows)
    frontier = [start]
    explored =[start]
    #Declare an empty list that will give the path
    bfsPath = {}
    while len(frontier) > 0:
        currCell = frontier.pop(0)
        if currCell == (1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1]- 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                if childCell in explored:
                    continue #Skip the next part of the code
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
            
            #Invert the bfsPAth as it is in the reverse path
    fwdPath = {}
    cell =(1,1)
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
    return fwdPath



#Create a new maze
m = maze(5,5)
m.CreateMaze()

path = BFS(m)
a = agent(m, footprints=True)
m.tracePath({a:path})

m.run()
