import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]

visited = [False] * (n+1)

distance = [INF] * (n+1)
distance[start] = 0

q = []

for _ in range(m):
    # a노드에서 b노드로 가는 cost c
    a, b, c = map(int, input().split())
    graph[a].append((b,c))


def dijkstra(graph, visited, distance, start):
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        info = heapq.heappop(q)
        if not visited[info[1]]:
            for node in graph[info[1]]:
                if not visited[node[0]]:
                    if distance[node[0]] >= INF:
                        distance[node[0]] = distance[info[1]] + node[1]
                    cost = distance[info[1]] + node[1]
                    if cost < distance[node[0]]:
                        distance[node[0]] = cost

                    heapq.heappush(q, (distance[node[0]], node[0]))
        visited[info[1]] = True
    return distance


distance = dijkstra(graph, visited, distance, start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

'''
6 11
1 
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''