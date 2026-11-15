# Problem C.1: Build and display adjacency list and adjacency matrix.


def build_adj_list(hubs, edges):
    """
    Input: list of hub names and list of undirected edges (u, v, length).
    Output: dict mapping each hub to sorted list of (neighbor, length) tuples.
    Complexity: Time O(V + E log E), Space O(V + E).
    """
    adj = {}
    for hub in hubs:
        adj[hub] = []

    for u, v, length in edges:
        adj[u].append((v, length))
        adj[v].append((u, length))

    # Uses list.sort() so neighbors of each hub are in alphabetical order (A -> H).
    for hub in hubs:
        adj[hub].sort()

    return adj


def build_adj_matrix(hubs, edges):
    """
    Input: list of hub names and list of undirected edges (u, v, length).
    Output: 8x8 matrix of road lengths (0 means no direct road).
    Complexity: Time O(V^2 + E), Space O(V^2).
    """
    n = len(hubs)
    hub_index = {}
    for idx in range(n):
        hub_index[hubs[idx]] = idx

    matrix = []
    for _ in range(n):
        matrix.append([0] * n)

    for u, v, length in edges:
        i = hub_index[u]
        j = hub_index[v]
        matrix[i][j] = length
        matrix[j][i] = length

    return matrix


def print_graph(hubs, adj_list, matrix):
    """Prints the adjacency list and 8x8 adjacency matrix cleanly."""
    print("Adjacency List (hub: neighbors with lengths):")
    for hub in hubs:
        items = []
        for neighbor, length in adj_list[hub]:
            items.append(neighbor + "(" + str(length) + ")")
        print("  " + hub + ": " + ", ".join(items))

    print("\nAdjacency Matrix (8x8 grid of lengths, 0 = no direct road):")
    print("    " + "  ".join(hubs))
    for i in range(len(hubs)):
        row_str = []
        for val in matrix[i]:
            row_str.append(str(val).rjust(2))
        print("  " + hubs[i] + " " + " ".join(row_str))
