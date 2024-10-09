import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice([255, 0], N*N, p=[0.2, 0.8]).reshape(N, N)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0, 0, 255],
                       [255, 0, 255],
                       [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider
    
def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + grid[(i-1)%N, j] + grid[(i+1)%N, j] + grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]) / 255)
            
            # apply Conway's rules
            if grid[i,j] == 255:
                if (total < 2) or (total > 3 ):
                    newGrid[i,j] = 0
            else:
                if total == 3:
                    newGrid[i,j] = 255
                        
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    # need to return a tuple here, since this callback function needs to return an iterable
    return img, 

def main():
    # initialize ArgumentParser object and add arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', dest='glider', action='store_true', required=False)
    parser.add_argument('--gosper', dest='gosper', action='store_true', required=False)
    args = parser.parse_args()
    
    # set grid size
    N = 100
    # set N if specified and valid
    if args.N and int(args.N) > 8:
        N = int(args.N)
    
    # set animation update interval
    updateInterval = 50
    if args.interval: 
        updateInterval = int(args.interval)
    
    # declare grid
    grid = np.array([])
    
    # check if glider demo flag specified
    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        addGlider(1, 1, grid)
    elif args.gosper:
        grid = np.zeros(N*N).reshape(N, N)
        addGosper(10, 10, grid)
    else:
        # populate grid with random on/off, more off than on
        grid = randomGrid(N)
    
    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N), interval=updateInterval, save_count=50)
    plt.show()
    return ani
    
if __name__ == '__main__':
    main()
