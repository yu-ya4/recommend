data = {
    "A": {
        "ナルニア": 1, "ハリポタ": 1, "広辞苑": 0, "指輪物語": 1, "統計学入門": 0
    },
    "B": {
        "ハリポタ": 0, "広辞苑": 1, "指輪物語": 0, "統計学入門": 1
    },
    "C": {
        "ナルニア": 1, "広辞苑": 0, "指輪物語": 1
    },
    "D": {
        "ナルニア": 1, "ハリポタ": 0, "広辞苑": 1, "統計学入門": 1
    },
    "E": {
        "ナルニア": 0, "広辞苑": 1, "指輪物語": 1, "統計学入門": 0
    },
}


# ジャカード係数を計算
def jaccard_similarity(x, y):
    intersection = len(x.intersection(y))
    union = len(x.union(y))
    return float(intersection / union)

