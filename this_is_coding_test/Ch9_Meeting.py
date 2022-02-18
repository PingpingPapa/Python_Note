INF = int(1e9)
n, m = map(int, input().split()) #회사의 개수, 경로의 개수
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

x, k = map(int, input().split())

def min_distance(visited, distance):
    min_val = INF
    index = 0
    for i in range(1, n+1):
        if not visited[i] and distance[i] < min_val:
            index = i
            min_val = distance[i]

    return index

def dijkstra(graph, start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    visited = [False] * (n + 1)


    for i in range(n-1):
        closest_city = min_distance(visited, distance)
        visited[closest_city] = True
        for city in graph[closest_city]:
            if distance[city] >= INF:
                distance[city] = distance[closest_city] + 1
            cost = distance[closest_city] + 1
            if cost < distance[city]:
                distance[city] = cost

    return distance

result = dijkstra(graph, 1)[k] + dijkstra(graph, k)[x]
if result >= INF :
    print(-1)
else:
    print(result)

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''