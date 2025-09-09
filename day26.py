from collections import defaultdict


def has_cycle(V, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * V

    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for i in range(V):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False


if __name__ == "__main__":
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        u, v = map(int, input().split())
        edges.append([u, v])

    print(has_cycle(V, edges))
