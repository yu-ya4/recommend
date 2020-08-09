from src.recommend.simple_cf import jaccard_similarity, get_similarity, get_recommends


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
