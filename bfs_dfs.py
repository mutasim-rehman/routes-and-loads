# Problem C.2 & C.3: BFS (hop distances) and DFS (visit order, components, cycle).

from collections import deque


def bfs(adj_list, start):
    """
    Input: adjacency list (sorted alphabetically) and start hub.
    Output: tuple (visit_order list, dict of hop distances from start).
    Complexity: Time O(V + E), Space O(V).
    """
    visited = set([start])
    dist = {start: 0}
    order = []
    queue = deque([start])

    while len(queue) > 0:
        current = queue.popleft()
        order.append(current)
        for neighbor, _ in adj_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                dist[neighbor] = dist[current] + 1
                queue.append(neighbor)

    return order, dist


def _dfs_visit(adj_list, u, visited, order):
    visited.add(u)
    order.append(u)
    for neighbor, _ in adj_list[u]:
        if neighbor not in visited:
            _dfs_visit(adj_list, neighbor, visited, order)


def dfs(adj_list, start):
    """
    Input: adjacency list (sorted alphabetically) and start hub.
    Output: list of hubs in DFS visit order starting from start.
    Complexity: Time O(V + E), Space O(V).
    """
    visited = set()
    order = []
    _dfs_visit(adj_list, start, visited, order)
    return order


def _cycle_dfs(adj_list, u, visited, active, parent, cycle_holder):
    visited.add(u)
    active.add(u)
    for v, _ in adj_list[u]:
        if v not in visited:
            parent[v] = u
            _cycle_dfs(adj_list, v, visited, active, parent, cycle_holder)
        elif v != parent[u] and v in active and len(cycle_holder) == 0:
            # Back-edge (u, v) found; trace parent links from u back to v.
            cycle = [v]
            curr = u
            while curr != v:
                cycle.append(curr)
                curr = parent[curr]
            cycle.append(v)
            cycle.reverse()
            cycle_holder.extend(cycle)
    active.remove(u)


def components_and_cycle(hubs, adj_list):
    """
    Input: list of hubs and adjacency list.
    Output: tuple (component_count, cycle_list_or_None).
    Complexity: Time O(V + E), Space O(V).
    """
    visited = set()
    components = 0
    cycle_holder = []

    for hub in hubs:
        if hub not in visited:
            components = components + 1
            parent = {hub: None}
            active = set()
            _cycle_dfs(adj_list, hub, visited, active, parent, cycle_holder)

    if len(cycle_holder) > 0:
        return components, cycle_holder
    return components, None
