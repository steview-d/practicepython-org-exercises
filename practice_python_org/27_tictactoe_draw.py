"""
Not continuing with this as have already done a tic-tac-toe game previously
and I'm just going over the same stuff.and
For original game, I have copied the code into exercise 29
Ignore all this below, I've abandoned it.
"""

grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
        
p1 = 'x'
p2 = 'o'
turn = 1


def draw_screen(grid_size = 3):
    # Convert to X & O's in grid
    screen_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for x in range(3):
        for y in range(3):
            if grid[x][y] == 0:
                screen_grid[x][y] = " "
            elif grid[x][y] == 1:
                screen_grid[x][y] = "X"
            else:
                screen_grid[x][y] = "O"
    
    print(' ---' * grid_size)
    for i in range(grid_size):
        print('| {} | {} | {} |'.format(screen_grid[i][0], screen_grid[i][1], screen_grid[i][2]))
        print(' ---' * grid_size)
    return

while True:
    # draw_screen()
    if turn == 1:
        turn = str(input("Your turn player one"))
        turn = turn.split(',')
