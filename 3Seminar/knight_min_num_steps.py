n = 5
x_start = 1
y_start = 1
x_end = 5
y_end = 5

def min_num_of_steps(n, x_start, y_start, x_end, y_end):
    boundaries = [i for i in range(n)]
    knight_positions_list = [[0 for _ in range(n)] for _ in range(n)]
    knight_positions_list[y_start - 1][x_start - 1] = 1
    flag = ''
    c = 0
    while flag != 'end':
        knight_positions_list_1 = [[0 for _ in range(n)] for _ in range(n)]
        for y in range(n):
            for x in range(n):
                if knight_positions_list[y][x] == 1:
                    if (y+2 in boundaries) and (x + 1 in boundaries):
                        knight_positions_list_1[y + 2][x + 1] = 1
                    if (y+1 in boundaries) and (x + 2 in boundaries):
                        knight_positions_list_1[y + 1][x + 2] = 1
                    if (y-1 in boundaries) and (x + 2 in boundaries):
                        knight_positions_list_1[y - 1][x + 2] = 1
                    if (y-2 in boundaries) and (x + 1 in boundaries):
                        knight_positions_list_1[y - 2][x + 1] = 1
                    if (y-2 in boundaries) and (x - 1 in boundaries):
                        knight_positions_list_1[y - 2][x - 1] = 1
                    if (y-1 in boundaries) and (x - 2 in boundaries):
                        knight_positions_list_1[y - 1][x - 2] = 1
                    if (y+1 in boundaries) and (x - 2 in boundaries):
                        knight_positions_list_1[y + 1][x - 2] = 1
                    if (y+2 in boundaries) and (x - 1 in boundaries):
                        knight_positions_list_1[y + 2][x - 1] = 1
        knight_positions_list = knight_positions_list_1
        c += 1
        if knight_positions_list[y_end - 1][x_end - 1] == 1:
            flag = 'end'
    return c

print(min_num_of_steps(n, x_start, y_start, x_end, y_end))
