def draw_screen(grid_size):
    print(' ---' * grid_size)
    for i in range(grid_size):
        print('|   ' * grid_size + '|')
        print(' ---' * grid_size)
    return


if __name__ == "__main__":
    draw_screen(3)