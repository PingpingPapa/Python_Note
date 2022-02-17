def dfs(graph, v, visited):
    visited[v] = 1

    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited)

# input()
n, m = map(int, input().split())
ice_frame = []
for _ in range(n):
    ice_frame.append(list(map(int,input())))

# make graph and visited
visited = []
graph= [[] for _ in range(n*m)]
for i in range(n):
    for j in range(m):
        visited.append(ice_frame[i][j])
        k = i*m+j
        if k == 0:
            graph[k].append(k+1)
            graph[k].append(k+m)
        elif k == m-1:
            graph[k].append(k-1)
            graph[k].append(k+m)
        elif k == m*(n-1):
            graph[k].append(k+1)
            graph[k].append(k-m)
        elif k == m*n-1:
            graph[k].append(k-1)
            graph[k].append(k-m)

        elif i == 0:
            graph[k].append(k-1)
            graph[k].append(k+1)
            graph[k].append(k+m)
        elif i == n-1:
            graph[k].append(k-1)
            graph[k].append(k+1)
            graph[k].append(k-m)
        elif j == 0:
            graph[k].append(k+1)
            graph[k].append(k-m)
            graph[k].append(k+m)
        elif j == m-1:
            graph[k].append(k-1)
            graph[k].append(k-m)
            graph[k].append(k+m)

        else:
            graph[k].append(k-1)
            graph[k].append(k+1)
            graph[k].append(k-m)
            graph[k].append(k+m)

cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i*m+j] == 0:
            cnt += 1
            dfs(graph, i*m+j, visited)



print("result:", cnt)
'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

'''

'''
3 3
010
111
010
'''
