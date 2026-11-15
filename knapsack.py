# Problem A: 0/1 Knapsack (top-down memoization, bottom-up tabulation, reconstruction).


def _knapsack_memo_helper(parcels, i, w, memo):
    # Base case: no parcels left or zero remaining capacity.
    if i == 0 or w == 0:
        return 0

    # Return cached result if already solved.
    if memo[i][w] != -1:
        return memo[i][w]

    _, weight, value = parcels[i - 1]
    if weight > w:
        # Parcel i is too heavy for remaining capacity w.
        memo[i][w] = _knapsack_memo_helper(parcels, i - 1, w, memo)
    else:
        # Best of skipping vs taking parcel i.
        skip_val = _knapsack_memo_helper(parcels, i - 1, w, memo)
        take_val = value + _knapsack_memo_helper(parcels, i - 1, w - weight, memo)
        memo[i][w] = max(skip_val, take_val)
    return memo[i][w]


def knapsack_top_down(parcels, capacity):
    """
    Input: parcels list of (id, weight, value), integer capacity W.
    Output: maximum total value achievable within capacity W.
    Complexity: Time O(n * W), Space O(n * W) for memo table + O(n) call stack.
    """
    n = len(parcels)
    memo = []
    for _ in range(n + 1):
        memo.append([-1] * (capacity + 1))
    return _knapsack_memo_helper(parcels, n, capacity, memo)


def knapsack_bottom_up(parcels, capacity):
    """
    Input: parcels list of (id, weight, value), integer capacity W.
    Output: tuple (max_value, 2D dp table of size (n+1) x (W+1)).
    Complexity: Time O(n * W), Space O(n * W).
    """
    n = len(parcels)
    table = []
    for _ in range(n + 1):
        table.append([0] * (capacity + 1))

    # Fill table row by row: i parcels considered, w current capacity.
    for i in range(1, n + 1):
        _, weight, value = parcels[i - 1]
        for w in range(1, capacity + 1):
            if weight > w:
                table[i][w] = table[i - 1][w]
            else:
                skip_val = table[i - 1][w]
                take_val = value + table[i - 1][w - weight]
                table[i][w] = max(skip_val, take_val)

    return table[n][capacity], table


def reconstruct_knapsack(parcels, capacity, table):
    """
    Input: parcels list, capacity W, filled 2D DP table.
    Output: list of chosen parcel tuples (id, weight, value) in original order.
    Complexity: Time O(n), Space O(n) for the chosen list.
    """
    chosen = []
    i = len(parcels)
    w = capacity

    # Trace backwards from (n, W): if value changed from row above, item i was taken.
    while i > 0 and w > 0:
        if table[i][w] != table[i - 1][w]:
            parcel = parcels[i - 1]
            chosen.append(parcel)
            w = w - parcel[1]
        i = i - 1

    chosen.reverse()
    return chosen
