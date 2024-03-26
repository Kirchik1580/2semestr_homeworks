edge_list = [
    [0,1],[0,2],[0,3],[1,4],[1,5],[2,4],[2,5],[2,6],[3,5],[3,6],[4,7],[5,7],[6,7],[1,2],[3,2]
]

vert_num = 8

adj_list = [[] for _ in range(vert_num)]

for edge in edge_list:
    u = edge[0]
    v = edge[1]
    adj_list[u].append(v)
adj_list

adj_matrix = [[0 for _ in range(vert_num)] for _ in range(vert_num)]

for edge in edge_list:#
    u = edge[0]
    v = edge[1]
    adj_matrix[u][v] = 1
adj_matrix

g = adj_list

colors = ['w' for _ in range(vert_num)]
parents = [None for _ in range(vert_num)]
timer = 0
tin = [None for _ in range(vert_num)]
tout = [None for _ in range(vert_num)]


def dfs(v, p=-1):
    global timer
    parents[v] = p
    colors[v] = 'g'
    timer += 1
    tin[v] = timer
    for u in g[v]:
        if colors[u] == 'g':
            print(f'found cycle {v} -> {u}')
            continue
        elif colors[u] == 'b':
            continue
        elif colors[u] == 'w':
            dfs(u, v)

    colors[v] = 'b'
    timer += 1
    tout[v] = timer

print(dfs(0))
print(colors)
print(parents)

flag_count = [None for _ in range(vert_num)]
ways_count = [0 for _ in range(vert_num)]

def num_of_ways2(start, end):
    dfs(start)
    flag_count[start] = 'f'
    ways_count[start] = 1
    if colors[end] == 'w':
        return 0
    else:
        for k in range(vert_num):
            for j in range(vert_num):
                c = 0
                for i in range(vert_num):
                    if colors[i] != 'w' and (adj_matrix[i][j] == 1) and flag_count[j] != 'f':
                        if flag_count[i] == 'f':
                            c += ways_count[i]
                        else:
                            if colors[i] != 'g':
                                c = 0
                                break
                if c != 0:
                    flag_count[j] = 'f'
                    ways_count[j] = c
        return ways_count[end]

print(num_of_ways2(0,7))
