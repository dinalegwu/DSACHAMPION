from collections import deque

def path_exists(graph, start, target):
    if start not in graph or target not in graph:
        return False

    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == target:
            return True

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(path_exists(graph, "A", "F"))
print(path_exists(graph, "D", "A"))