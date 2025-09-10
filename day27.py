from collections import deque, defaultdict


def shortest_path(V, edges, start, end):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * V
    distance = [-1] * V

    queue = deque([start])
    visited[start] = True
    distance[start] = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return distance[end]


if __name__ == "__main__":
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        u, v = map(int, input().split())
        edges.append([u, v])

    start, end = map(int, input().split())

    print(shortest_path(V, edges, start, end))
