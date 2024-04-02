n = 5
x_start = 1
y_start = 1
x_end = 4
y_end = 5
BIG_n = 10000000

x_start = x_start - 1
y_start = y_start - 1
x_end = x_end - 1
y_end = y_end - 1
def construct_knight_ways(n, x_start, y_start):
    flag = ''
    boundaries = [i for i in range(n)]
    m = []
    m.append([[y_start,x_start],[y_start,x_start]])
    matrix_of_positions = [[0 for _ in range(n)] for _ in range(n)]
    matrix_of_positions[0][0] = 1
    while flag != 'end':
        for i in m:
            y0 = i[1][0]
            x0 = i[1][1]
            if (y0 + 2 in boundaries) and (x0 + 1 in boundaries) and (not matrix_of_positions[y0 + 2][x0 + 1] == 1):
                m.append([[y0, x0],[y0 + 2, x0 + 1]])
                matrix_of_positions[y0 + 2][x0 + 1] = 1
            if (y0 + 1 in boundaries) and (x0 + 2 in boundaries) and (not matrix_of_positions[y0 + 1][x0 + 2] == 1):
                m.append([[y0, x0],[y0 + 1, x0 + 2]])
                matrix_of_positions[y0 + 1][x0 + 2] = 1
            if (y0 - 1 in boundaries) and (x0 + 2 in boundaries) and (not matrix_of_positions[y0 - 1][x0 + 2] == 1):
                m.append([[y0, x0],[y0 - 1, x0 + 2]])
                matrix_of_positions[y0 - 1][x0 + 2] = 1
            if (y0 - 2 in boundaries) and (x0 + 1 in boundaries) and (not matrix_of_positions[y0 - 2][x0 + 1] == 1):
                m.append([[y0, x0],[y0 - 2, x0 + 1]])
                matrix_of_positions[y0 - 2][x0 + 1] = 1
            if (y0 - 2 in boundaries) and (x0 - 1 in boundaries) and (not matrix_of_positions[y0 - 2][x0 - 1] == 1):
                m.append([[y0, x0],[y0 - 2, x0 - 1]])
                matrix_of_positions[y0 - 2][x0 - 1] = 1
            if (y0 - 1 in boundaries) and (x0 - 2 in boundaries) and (not matrix_of_positions[y0 - 1][x0 - 2] == 1):
                m.append([[y0, x0],[y0 - 1, x0 - 2]])
                matrix_of_positions[y0 - 1][x0 - 2] = 1
            if (y0 + 1 in boundaries) and (x0 - 2 in boundaries) and (not matrix_of_positions[y0 + 1][x0 - 2] == 1):
                m.append([[y0, x0],[y0 + 1, x0 - 2]])
                matrix_of_positions[y0 + 1][x0 - 2] = 1
            if (y0 + 2 in boundaries) and (x0 - 1 in boundaries) and (not matrix_of_positions[y0 + 2][x0 - 1] == 1):
                m.append([[y0, x0],[y0 + 2, x0 - 1]])
                matrix_of_positions[y0 + 2][x0 - 1] = 1
        flag = 'end'
        for u in matrix_of_positions:
            for v in u:
                if v == 0:
                    flag = ''
    m = m[1:len(m)]
    return m

edge_list = construct_knight_ways(n, x_start, y_start)


def construct_adj_list(edge_list, v_n):
    adj_list = [[[] for _ in range(v_n)] for _ in range(v_n)]
    for edge in edge_list:
        srcy = edge[0][0]
        srcx = edge[0][1]
        dest = edge[1]
        adj_list[srcy][srcx].append(dest)
    return adj_list

adj_list = construct_adj_list(edge_list, n)


def bfs(adj_list, x_start, y_start):
    srcy = y_start
    srcx = x_start
    v_n = len(adj_list)
    dist = [[BIG_n for _ in range(v_n)] for _ in range(v_n)]

    dist[srcy][srcx] = 0

    queue = []
    queue.append([srcy,srcx])
    while len(queue) != 0:
        u = queue.pop(0)
        y2 = u[0]
        x2 = u[1]
        for y1, x1 in adj_list[y2][x2]:
            if dist[y1][x1] == BIG_n:
                dist[y1][x1] = dist[y2][x2] + 1
                queue.append([y1,x1])

    return dist

bfs_result = bfs(adj_list, x_start, y_start)
print(bfs_result[y_end][x_end])
