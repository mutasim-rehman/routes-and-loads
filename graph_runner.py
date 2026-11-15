# Helper runner to print outputs for graph Problems C, D, and E.

from data import HUBS, EDGES
from graph_build import build_adj_list, build_adj_matrix, print_graph
from bfs_dfs import bfs, dfs, components_and_cycle
from shortest_path import dijkstra, reconstruct_path
from mst import kruskal_mst


def run_graph_problems(start_hub):
    """Runs and prints Problems C, D, and E for the given start_hub."""
    adj_list = build_adj_list(HUBS, EDGES)
    adj_matrix = build_adj_matrix(HUBS, EDGES)

    print("\n=== PROBLEM C: Road Map (Representation, BFS, DFS) ===")
    print_graph(HUBS, adj_list, adj_matrix)

    bfs_order, hop_dist = bfs(adj_list, start_hub)
    print("\nBFS visit order from", start_hub + ":", " -> ".join(bfs_order))
    print("Hop distances from", start_hub + ":")
    for hub in HUBS:
        print("  " + hub + ": " + str(hop_dist[hub]))

    dfs_order = dfs(adj_list, start_hub)
    print("\nDFS visit order from", start_hub + ":", " -> ".join(dfs_order))
    comp_count, cycle = components_and_cycle(HUBS, adj_list)
    print("Connected components:", comp_count)
    print("Is graph connected?", comp_count == 1)
    if cycle is not None:
        print("Contains cycle? Yes, e.g.:", " -> ".join(cycle))
    else:
        print("Contains cycle? No")
    print("Smallest number of roads from", start_hub, "to H:", hop_dist["H"])

    print("\n=== PROBLEM D: Shortest Routes (Dijkstra) ===")
    dist, parent = dijkstra(adj_list, start_hub)
    print("Shortest-path distances from", start_hub + ":")
    for hub in HUBS:
        print("  " + hub + ": " + str(dist[hub]))
    path_to_h = reconstruct_path(parent, start_hub, "H")
    print("Shortest path from", start_hub, "to H:", " -> ".join(path_to_h))

    print("\n=== PROBLEM E: The Backbone (Kruskal MST) ===")
    mst_edges, total_len = kruskal_mst(HUBS, EDGES)
    print("MST edges chosen:")
    for u, v, length in mst_edges:
        print("  " + u + " - " + v + " (length " + str(length) + ")")
    print("Total MST cable length:", total_len)
