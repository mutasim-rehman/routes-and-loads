# Problem B: Coin Change (bottom-up DP with reconstruction, and greedy comparison).


def coin_change_dp(coins, target):
    """
    Input: list of coin denominations, integer target amount T.
    Output: tuple (min_coins, list_of_coins_used); (-1, []) if impossible.
    Complexity: Time O(k * T) where k = len(coins), Space O(T).
    """
    # Sentinel value larger than any possible coin count (max needed is T ones).
    impossible = target + 1
    dp = [impossible] * (target + 1)
    choice = [-1] * (target + 1)
    dp[0] = 0

    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount and dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1
                choice[amount] = coin

    if dp[target] == impossible:
        return -1, []

    # Reconstruct the coins used by walking backwards from target.
    used_coins = []
    rem = target
    while rem > 0:
        c = choice[rem]
        used_coins.append(c)
        rem = rem - c

    return dp[target], used_coins


def coin_change_greedy(coins, target):
    """
    Input: list of coin denominations, integer target amount T.
    Output: tuple (coin_count, list_of_coins_used); (-1, []) if remainder > 0.
    Complexity: Time O(k log k + T), Space O(T) in the worst case.
    """
    # Uses Python's sorted() to sort coins descending (largest first).
    desc_coins = sorted(coins, reverse=True)
    rem = target
    used_coins = []

    for coin in desc_coins:
        while coin <= rem:
            used_coins.append(coin)
            rem = rem - coin

    if rem != 0:
        return -1, []
    return len(used_coins), used_coins


def find_greedy_mismatch(coins, max_amount):
    """
    Input: coin denominations and search upper bound max_amount.
    Output: first (amount, dp_result, greedy_result) where DP beats greedy, or None.
    Complexity: Time O(max_amount * k * max_amount), Space O(max_amount).
    """
    for amt in range(1, max_amount + 1):
        dp_count, dp_coins = coin_change_dp(coins, amt)
        gr_count, gr_coins = coin_change_greedy(coins, amt)
        if dp_count != -1 and (gr_count == -1 or dp_count < gr_count):
            return amt, (dp_count, dp_coins), (gr_count, gr_coins)
    return None
