# Entry point for Assignment 3: Routes & Loads.
# Run with: py main.py (reads last_3_digits from .env) or py main.py <seed>

import sys
from data import load_seed_from_env, PARCELS, COINS, get_personal_params
from knapsack import knapsack_top_down, knapsack_bottom_up, reconstruct_knapsack
from coin_change import coin_change_dp, coin_change_greedy, find_greedy_mismatch
from graph_runner import run_graph_problems


def run_dp_problems(capacity_w, target_t):
    """Runs and prints Problems A and B."""
    print("\n=== PROBLEM A: The Van Loader (0/1 Knapsack) ===")
    top_val = knapsack_top_down(PARCELS, capacity_w)
    bot_val, table = knapsack_bottom_up(PARCELS, capacity_w)
    chosen = reconstruct_knapsack(PARCELS, capacity_w, table)

    print("Capacity W:", capacity_w)
    print("Top-down memoization max value:", top_val)
    print("Bottom-up tabulation max value:", bot_val)
    print("Both implementations match?", top_val == bot_val)

    total_wt = 0
    ids = []
    for name, wt, val in chosen:
        ids.append(name + "(w=" + str(wt) + ", v=" + str(val) + ")")
        total_wt = total_wt + wt
    print("Chosen parcels:", ", ".join(ids))
    print("Total weight loaded:", total_wt, "/", capacity_w)

    print("\n=== PROBLEM B: Making Change (Coin Change) ===")
    dp_count, dp_coins = coin_change_dp(COINS, target_t)
    gr_count, gr_coins = coin_change_greedy(COINS, target_t)

    print("Target T:", target_t, "| Denominations:", COINS)
    print("DP minimum coins:", dp_count, "| Coins used:", dp_coins)
    print("Greedy coin count:", gr_count, "| Coins used:", gr_coins)
    print("Does greedy match DP on T?", dp_count == gr_count)

    mismatch = find_greedy_mismatch(COINS, 30)
    if mismatch is not None:
        amt, dp_res, gr_res = mismatch
        print("Counterexample amount:", amt)
        print("  DP:", dp_res[0], "coins ->", dp_res[1])
        print("  Greedy:", gr_res[0], "coins ->", gr_res[1])


def main():
    seed = load_seed_from_env()
    if len(sys.argv) > 1:
        seed = int(sys.argv[1])

    params = get_personal_params(seed)
    print("=== PERSONAL PARAMETERS ===")
    print("s =", params["s"], "| W =", params["W"],
          "| T =", params["T"], "| Start hub =", params["start_hub"])

    run_dp_problems(params["W"], params["T"])
    run_graph_problems(params["start_hub"])


if __name__ == "__main__":
    main()
