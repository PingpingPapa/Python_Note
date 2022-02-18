INF = int(1e9)
import heapq
import sys
input = sys.stdin.readline

n, m, c = map(int, input().split()) #도시의 수, 통로의 수, 출발 도시
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

q = []

def dijkstra(graph, visited, start, distance):
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))

    while q:
        pop = heapq.heappop(q)
        visited[pop[1]] = True
        for info in graph[pop[1]]:
            # pop 도시와 인접한 도시들의 거리를 수정하자
            if distance[info[0]] >= INF:
                distance[info[0]] = distance[pop[1]] + info[1]
            cost = distance[pop[1]] + info[1]
            if distance[info[0]] > cost:
                distance[info[0]] = cost

            if not visited[info[0]]:
                heapq.heappush(q, (distance[info[0]], info[0]))

    return distance, visited

dis, visited = dijkstra(graph, visited, c, distance)
for i in range(len(dis)):
    if dis[i] >= INF:
        dis[i] = 0

print(visited.count(True)-1, max(dis))

'''
3 2 1
1 2 4
1 3 2

6 10 1
1 2 1
1 3 6
1 4 2
2 4 5
3 5 7
3 4 8
4 1 3
4 2 4
4 5 9
6 5 8

'''