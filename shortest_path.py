# Problem D: Dijkstra's shortest paths and path reconstruction.

import heapq


def dijkstra(adj_list, start):
    """
    Input: weighted adjacency list and start hub.
    Output: tuple (dist dict, parent dict for predecessor tracking).
    Complexity: Time O((V + E) log V) using heapq, Space O(V).
    """
    dist = {}
    parent = {}
    for hub in adj_list:
        dist[hub] = float("inf")
        parent[hub] = None

    dist[start] = 0
    # Min-heap stores (distance_so_far, hub).
    pq = [(0, start)]

    while len(pq) > 0:
        curr_dist, u = heapq.heappop(pq)

        # Skip stale heap entries that are worse than known shortest distance.
        if curr_dist > dist[u]:
            continue

        for neighbor, weight in adj_list[u]:
            new_dist = curr_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = u
                heapq.heappush(pq, (new_dist, neighbor))

    return dist, parent


def reconstruct_path(parent, start, target):
    """
    Input: predecessor dict, start hub, target hub.
    Output: list of hubs on shortest path from start to target (or [] if unreachable).
    Complexity: Time O(V), Space O(V).
    """
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    path.reverse()
    if len(path) == 0 or path[0] != start:
        return []
    return path
