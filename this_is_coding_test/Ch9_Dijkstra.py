import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]

visited = [False] * (n+1)
visited[0] = True
visited[start] = True

distance = [INF] * (n+1)
distance[start] = 0

for _ in range(m):
    # a노드에서 b노드로 가는 cost c
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드
def not_visited_nearest_node(visited, distance):
    min_val = INF
    index = 0
    for i in range(1, 1+n):
        if not visited[i] and distance[i] < min_val:
            index = i
            min_val = distance[i]

    return index

def dijkstra(graph, visited, distance, start):
    distance[start] = 0
    visited[start] = True

    for info in graph[start]:
        distance[info[0]] = info[1]

    for i in range(n-1):
        now = not_visited_nearest_node(visited, distance)
        visited[now] = True
        for info in graph[now]:
            if distance[info[0]] >= INF:
                distance[info[0]] = info[1] + distance[now]

            cost = distance[info[0]] + info[1]

            if cost < distance[info[0]]:
                distance[info[0]] = cost
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