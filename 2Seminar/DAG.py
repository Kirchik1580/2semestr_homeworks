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


def topsort():
    for v in range(vert_num):
        if colors[v] == 'w':
            dfs(v)
        vert_list = [i for i in range(vert_num)]
        ans = [x for y,x in sorted(zip(tout, vert_list), key = lambda pair: pair[0], reverse = True)]
        return ans

ts = topsort()
print(ts)

def num_of_ways(start, end):
    ways_count[start] = 1
    for j in ts:
        for i in range(vert_num):
            if adj_matrix[i][j] == 1:
                ways_count[j] += ways_count[i]

    return ways_count[end]

print(num_of_ways(0,7))

