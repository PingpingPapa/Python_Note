import itertools
INF = int(1e9)


n = int(input()) # node
m = int(input()) # edge

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, n+1):
    lst = [j for j in range(1, i)] + [j for j in range(i+1,n+1)]
    for sets in itertools.permutations(lst, r=2):
        graph[sets[0]][sets[1]] = min(graph[sets[0]][sets[1]], graph[sets[0]][i] + graph[i][sets[1]])

for i in range(1, len(graph)):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print("INF", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''
