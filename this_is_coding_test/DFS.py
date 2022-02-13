graph_Adjacency_list = [[] for _ in range(9)]

graph_Adjacency_list[1].append(2)
graph_Adjacency_list[1].append(3)
graph_Adjacency_list[1].append(8)

graph_Adjacency_list[2].append(1)
graph_Adjacency_list[2].append(7)

graph_Adjacency_list[3].append(1)
graph_Adjacency_list[3].append(4)
graph_Adjacency_list[3].append(5)

graph_Adjacency_list[4].append(3)
graph_Adjacency_list[4].append(5)

graph_Adjacency_list[5].append(3)
graph_Adjacency_list[5].append(4)

graph_Adjacency_list[6].append(7)

graph_Adjacency_list[7].append(2)
graph_Adjacency_list[7].append(6)
graph_Adjacency_list[7].append(8)

graph_Adjacency_list[8].append(1)
graph_Adjacency_list[8].append(7)

print("graph", graph_Adjacency_list)

visit = [1, 0,0,0,0,0,0,0,0]
stack = []

def DFS(graph, start, stack, visit):
    visit[start] = 1
    stack.append(start)

    for node in graph[stack[-1]]:
        if not visit[node]:
            print(node)
            DFS(graph, node, stack, visit)

    if sum(visit) == len(visit):
        print("DFS Ends")

stack2 = [1]

def DFS2(graph, stack2, visit):
    if sum(visit) == len(visit):
        print("DFS Ends")
        return None

    visit[stack2[-1]] = 1
    print(stack2[-1])

    for node in graph[stack2[-1]]:
        if not visit[node]:
            stack2.append(node)
            return DFS2(graph, stack2, visit)

    stack2.pop()
    DFS2(graph, stack2, visit)

DFS2(graph_Adjacency_list, stack2, visit)