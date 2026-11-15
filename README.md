# Assignment 3: Routes & Loads

Simple, modular Python implementation of Problems A–E for **Design and Analysis of Algorithms**.

## Files
- `data.py` — Reads `last_3_digits` from `.env`, computes personal parameters (`s`, `W`, `T`, `start_hub`), and stores fixed datasets.
- `knapsack.py` — Problem A: Top-down memoization, bottom-up 2D tabulation, and parcel reconstruction.
- `coin_change.py` — Problem B: Bottom-up DP coin change with reconstruction, greedy comparison, and counterexample finder.
- `graph_build.py` — Problem C.1: Adjacency list and 8x8 adjacency matrix builders and printer.
- `bfs_dfs.py` — Problem C.2–C.3: BFS (visit order & hop distances), DFS (visit order), connected components, and cycle detection.
- `shortest_path.py` — Problem D: Dijkstra's algorithm (`heapq`) and predecessor path reconstruction.
- `mst.py` — Problem E: Kruskal's MST algorithm with custom Union-Find (`find_root`, `union_sets`).
- `graph_runner.py` — Runs and prints outputs for Problems C, D, and E.
- `main.py` — Main entry point that prints personal parameters and runs Problems A–E.
- `demo.ipynb` — Interactive demo notebook with EDA, sample input/output comparisons, DP heatmap, and network/MST/Dijkstra visualizations.

## Allowed Python Helpers Used
- `collections.deque` in `bfs_dfs.py` for the BFS queue.
- `heapq` in `shortest_path.py` for Dijkstra's priority queue.
- `sorted()` in `coin_change.py` (sorting coins descending for greedy) and `mst.py` (sorting edges by weight for Kruskal).
- `list.sort()` in `graph_build.py` (sorting each hub's neighbors alphabetically `A -> H`).

## How to Run
1. Set `last_3_digits = <your_3_digits>` in `.env` (currently `514`).
2. Run the main script (reads `.env` automatically):
   ```bash
   python3 main.py
   ```
   On Windows with the Python launcher:
   ```bash
   py main.py
   ```
   You can also pass a different seed on the command line (e.g., `py main.py 605`).
3. For the visual demo, EDA, sample input/output tables, and charts, open and run `demo.ipynb` in Jupyter / VS Code.
