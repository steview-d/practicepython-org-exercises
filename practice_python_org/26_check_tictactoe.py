grid_one = [[0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]]
grid_two = [[0, 0, 1],
            [0, 0, 1],
            [0, 0, 1]]
grid_three = [[2, 0, 0],
            [2, 0, 0],
            [2, 0, 0]]
grid_four = [[0, 0, 0],
            [0, 0, 0],
            [2, 2, 2]]
grid_five = [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]
grid_six = [[0, 0, 2],
            [0, 2, 0],
            [2, 0, 0]]
            
grids = [grid_one, grid_two, grid_three, grid_four, grid_five, grid_six]
            
def check_winner_old(grid, player):
    
    win = '{}'.format(player) * 3
    
    # Horizontal Check
    for x in grid:
        line = ''
        for i in x:
            line += str(i)
        if win == line:
            return True
    
    # Vertical Check
    for y in range(0, 3):
        line = ''
        for i in grid:
            line += str(i[y])
        if win == line:
            return True
    
    # Diagonal Check
    line = '{}{}{}'.format(grid[0][0], grid[1][1], grid[2][2])
    if win == line:
        return True
    line = '{}{}{}'.format(grid[2][0], grid[1][1], grid[0][2])
    if win == line:
        return True

    return False


def check_winner(grid, player):
    # Check Rows
    for x in range(0, 3):
        row = set([grid[x][0], grid[x][1], grid[x][2]])
        if len(row) == 1 and row == set([player]):
            return True
            
    # Check Columns
    for y in range(0, 3):
        column = set([grid[0][y], grid[1][y], grid[2][y]])
        if len(column) == 1 and column == set([player]):
            return True
    
    # Check Diagonals
    
    d1 = set([grid[0][0], grid[1][1], grid[2][2]])
    d2 = set([grid[2][0], grid[1][1], grid[0][2]])
    
    for x in d1, d2:
        if len(x) == 1 and x == set([player]):
            return True

    return False
        

if __name__ == "__main__":
    for i in grids:
        for x in range(1, 3):
            print(check_winner(i, x))
