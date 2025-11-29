from collections import deque

def shortest_path(rooms, doors, start, goal):
    """
    Compute one shortest path between start and goal in an undirected graph.

    rooms: list of room name strings.
    doors: list of (a, b) pairs, each pair is an undirected door between rooms a and b.
    start: start room name.
    goal: goal room name.

    Return:
      - list of room names from start to goal (inclusive) for one shortest path,
      - [start] if start == goal,
      - [] if no path exists.
    """

    # Step 7: Edge case
    if start == goal:
        if start in rooms:
            return [start]
        return []

    if not rooms:
        return []

    # Step 1–3: Build adjacency list
    graph = {room: [] for room in rooms}
    for a, b in doors:
        graph[a].append(b)
        graph[b].append(a)

    # Step 4–6: BFS
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # If goal not reached
    if goal not in parent:
        return []

    # Reconstruct path
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()
    return path
