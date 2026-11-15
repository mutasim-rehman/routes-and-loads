# Problem E: Kruskal's Minimum Spanning Tree with Union-Find.


def _edge_weight(edge):
    return edge[2]


def find_root(parent, node):
    """
    Input: parent dict and node label.
    Output: root representative of node's set (with path compression).
    Complexity: Time O(alpha(V)) amortized, Space O(1) extra.
    """
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node


def union_sets(parent, rank, u, v):
    """
    Input: parent dict, rank dict, two hubs u and v.
    Output: True if u and v were merged (different sets), False if already connected.
    Complexity: Time O(alpha(V)) amortized, Space O(1).
    """
    root_u = find_root(parent, u)
    root_v = find_root(parent, v)

    if root_u == root_v:
        return False

    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] = rank[root_u] + 1
    return True


def kruskal_mst(hubs, edges):
    """
    Input: list of hubs and list of weighted edges (u, v, length).
    Output: tuple (list of MST edges, total MST length).
    Complexity: Time O(E log E), Space O(V + E).
    """
    parent = {}
    rank = {}
    for hub in hubs:
        parent[hub] = hub
        rank[hub] = 0

    # Uses Python's sorted() to sort edges from shortest to longest.
    sorted_edges = sorted(edges, key=_edge_weight)
    mst_edges = []
    total_length = 0

    for u, v, length in sorted_edges:
        if union_sets(parent, rank, u, v):
            mst_edges.append((u, v, length))
            total_length = total_length + length
            if len(mst_edges) == len(hubs) - 1:
                break

    return mst_edges, total_length
