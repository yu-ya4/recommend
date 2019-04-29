"""
Simple Collaborative Filtering.
An user based model.

recommends = get_recommends("C")
> [('ハリポタ', 0.6666666666666666), ('統計学入門', 0.27272727272727276)]
"""

all_items = {"ナルニア", "ハリポタ", "広辞苑", "指輪物語", "統計学入門"}

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


# ジャッカード係数を計算
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


# 協調フィルタリングを用いて算出された推薦（ランキング）を得る
def get_recommends(user):
    # 対象ユーザがまだ推薦されていないアイテムの集合：推薦対象アイテム
    new_items = all_items - set(data[user].keys())
    # 推薦対象アイテムの予測評価値を入れる箱
    sum_scores = {item: 0.0 for item in new_items}
    sum_sim = {item: 0 for item in new_items}
    # # 対象ユーザ以外のユーザ
    others = list(data.keys()); others.remove(user)

    for other in others:
        sim = get_similariy(user, other)

        for new_item in new_items:
            if new_item in data[other]:
                # "評価値" × "類似度" を推薦度のスコアとして，全ユーザについて合計する
                sum_scores[new_item] += data[other][new_item] * sim
                # アイテムごとのユーザの類似度の合計を計算しておき，上記のスコアを割る（加重平均のイメージ）
                sum_sim[new_item] += sim

    recommends = {item: sum_scores[item] / sum_sim[item] for item in new_items}
    recommends = sorted(recommends.items(), key=lambda x:x[1], reverse=True)

    return recommends
