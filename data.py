# Personal parameters and fixed datasets for Assignment 3 (Routes & Loads).

import os

# Fallback seed if .env is missing or no CLI argument is given.
DEFAULT_SEED = 514


def load_seed_from_env(env_path=".env"):
    """
    Input: path to .env file.
    Output: integer last_3_digits if found, otherwise DEFAULT_SEED.
    Complexity: Time O(L) where L = lines in .env, Space O(1).
    """
    if not os.path.exists(env_path):
        return DEFAULT_SEED

    with open(env_path, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()
            if line == "" or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            if key.strip() == "last_3_digits":
                return int(val.strip().strip('"').strip("'"))

    return DEFAULT_SEED

# Eight city hubs indexed 0..7 (A=0 ... H=7).
HUBS = ["A", "B", "C", "D", "E", "F", "G", "H"]

# Parcel list for Problem A (0/1 Knapsack): (parcel_id, weight, value)
PARCELS = [
    ("P1", 2, 3),
    ("P2", 3, 4),
    ("P3", 4, 5),
    ("P4", 5, 7),
    ("P5", 6, 8),
    ("P6", 7, 10),
    ("P7", 9, 13),
    ("P8", 10, 15),
]

# Non-standard coin denominations for Problem B (Coin Change).
COINS = [1, 3, 4, 9]

# Undirected weighted roads for Problems C, D, E: (hub1, hub2, length)
EDGES = [
    ("A", "B", 4),
    ("A", "C", 3),
    ("B", "C", 1),
    ("B", "D", 2),
    ("C", "D", 4),
    ("C", "E", 8),
    ("D", "E", 2),
    ("D", "F", 6),
    ("E", "F", 3),
    ("E", "G", 7),
    ("F", "G", 2),
    ("F", "H", 5),
    ("G", "H", 4),
]


def get_personal_params(seed):
    """
    Input: seed (int, last 3 digits of roll number).
    Output: dict with W (van capacity), T (change target), start_hub (str).
    Complexity: Time O(1), Space O(1).
    """
    capacity_w = 15 + (seed % 10)
    target_t = 30 + (seed % 20)
    start_hub = HUBS[seed % 8]
    return {
        "s": seed,
        "W": capacity_w,
        "T": target_t,
        "start_hub": start_hub,
    }
