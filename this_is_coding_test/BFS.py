from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])

    visited[start] = True
    print(start, end=' ')

    while queue:
        pop = queue.popleft()
        for i in graph[pop]:
            if not visited[i]:
                print(i, end=' ')
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9
start = 1
BFS(graph, start, visited)