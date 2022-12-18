import copy
import argparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# setting up the values for the grid
ON = 255
OFF = 0
vals = [ON, OFF]

def update(frameNum, img, grid):
    nextG = copy.deepcopy(grid)
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            # Return neighbours as list
            neighbours = []
            for xCheck in range(-1,2):
                for yCheck in range(-1,2):
                    # Out of grid x
                    if (x + xCheck) < 0 or (x + xCheck) >= len(grid[0]):
                        continue
                    elif (y + yCheck) < 0 or (y + yCheck) >= len(grid):
                        continue
                    else:
                        neighbours.append([x + xCheck, y + yCheck])
            neighbours.remove([x,y])

            # Assign heat value to cell
            heat = 0
            for cell in neighbours:
                t1 = cell[0]
                t2 = cell[1]
                if grid[t2][t1] == 1:
                    heat += 1
            if grid[y][x] == 1: 
                if heat == 2 or heat == 3:
                    nextG[y][x] = 1
                else:
                    nextG[y][x] = 0
            else:
                if heat == 3:
                    nextG[y][x] = 1
                else:
                    nextG[y][x] = 0
    # update data
    img.set_data(nextG)
    grid[:] = nextG[:]
    return img,

def init():
    with(open("input.txt", "r") as txt):
        lines = txt.read().splitlines()
        grid = []
        # Initialise grid
        for line in range(len(lines)):
            grid.append([])
            n = lines[line].split()
            for num in n:
                grid[line].append(int(num))
        return grid

def main():

    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
 
    # add arguments
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    args = parser.parse_args()
     
    # set grid size
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)
         
    # set animation update interval
    updateInterval = 10
    if args.interval:
        updateInterval = int(args.interval)

 
    # declare grid
    grid = init()

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, ),
                                  frames = 40,
                                  interval=updateInterval,
                                  save_count=50)
 
    # # of frames?
    # set output file
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])
 
    plt.show()

if __name__ == "__main__":
    main()

            



