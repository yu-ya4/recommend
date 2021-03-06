from src.recommend.simple_cf import (
    jaccard_similarity,
    get_similarity,
    get_recommends,
)


def test_jaccard_similarity() -> None:
    a = set([1, 2, 3])
    b = set([4, 5])
    c = set([2, 3, 4])

    res1 = jaccard_similarity(x=a, y=a)
    assert res1 == 1.0, "The similarity between the same sets must be 1.0."

    res2 = jaccard_similarity(x=a, y=b)
    assert (
        res2 == 0.0
    ), "The similarity between sets that do not have any common elements must be 0.0."

    res3 = jaccard_similarity(x=a, y=c)
    assert res3 == 0.5, "The similarity between {1, 2, 3} and {2, 3, 4} must be 0.5."


def test_get_similarity() -> None:
    res1 = get_similarity(user1="A", user2="A")
    assert res1 == 1.0, "The similarity between the same users must be 1.0."

    res2 = get_similarity(user1="A", user2="B")
    assert (
        res2 == 0.0
    ), "The similarity between users that have no common interests must be 1.0."

    res3 = get_similarity(user1="A", user2="C")
    assert res3 == 1.0, "The similarity between userA and userC must be 1.0."

    res4 = get_similarity(user1="A", user2="D")
    assert res4 == 0.25, "The similarity between userA and userD must be 0.25."


def test_get_recommend() -> None:
    res = get_recommends("C")
    assert res == [
        ("ハリポタ", 0.6666666666666666),
        ("統計学入門", 0.27272727272727276),
    ], "The recommended items for userC are not correct."
