from collections import deque

def BFS(graph, start, visited,end):
    queue = deque([start])
    result = [start]
    visited[start] = True
 #   print(start, end=' ')

    while queue:
        pop = queue.popleft()
        for i in graph[pop]:


            if i == end-1:
#                print("catch")
                return result
            if not visited[i]:
                result.append(i)
  #              print(i, end=' ')
                queue.append(i)
                visited[i] = True

def dfs(graph, v, visited, depth):
    visited[v] = True
    depth += 1
#    print("v:{}, depth:{}".format(v, depth))
    if v == 0:
        print("answer:", depth)
    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited, depth)

# input()
n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int,input())))

# make graph and visited
visited = []
graph= [[] for _ in range(n*m)]

for i in range(n):
    for j in range(m):
        visited.append(1-maze[i][j])
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



#for i in range(len(graph)):
#    print(i, graph[i])


v = BFS(graph, 0, visited, m*n)
#print("v:",sorted(v))
for i in range(len(visited)):
    if i in v:
        visited[i] = 0
    else:
        visited[i] = 1

#for i in range(int(len(visited)/m)):
#    print(visited[i*m:i*m+m])

dfs(graph,m*n-1,visited,0)
'''
5 6
101011
111111
000001
111111
111111
'''

'''
6 6
101011
111111
000001
111111
100000
111111
'''

'''
2 6
101011
111111
'''

'''
6 6
101011
111111
000001
111111
100001
111111
'''