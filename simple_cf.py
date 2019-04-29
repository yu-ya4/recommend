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


# 過去の行動履歴に基づいた 2 ユーザの類似度を計算
def get_similariy(user1, user2):

    # ユーザの行動履歴
    history1 = data[user1]
    history2 = data[user2]

    # 両方とものユーザに推薦されたアイテムの集合をとる。
    recommended_items1 = set(history1.keys())
    recommended_items2 = set(history2.keys())
    recommended_both = recommended_items1.intersection(recommended_items2)

    #両方ともに推薦されたアイテムがなければ類似度 0 とする。
    if len(recommended_both) == 0:
        return 0.0

    # 両方とものユーザに推薦されていてかつ，購入したアイテムの集合をとる。
    possitive_items1 = set([key for key, val in history1.items() if key in recommended_both and val == 1])
    possitive_items2 = set([key for key, val in history2.items() if key in recommended_both and val == 1])

    return jaccard_similarity(possitive_items1, possitive_items2)

