import pytest
from AppleMusicPods import Podcasts


def main():
    test_inspect()
    test_search()

def test_search():
    podcast = Podcasts("Robert William Fisher")
    pdict = podcast.search_episodes()

    assert isinstance(pdict, dict)
    assert "results" in pdict
    assert isinstance(pdict["results"], list)
    assert pdict.get("resultCount", 0) > 0

    first_ep = pdict["results"][0]
    assert isinstance(first_ep, dict)
    assert "trackName" in first_ep
    assert "collectionName" in first_ep
    assert isinstance(first_ep["trackName"], str)
    assert isinstance(first_ep["collectionName"], str)


def test_inspect():
    podcast = Podcasts("Robert William Fisher")
    pdict = podcast.search_episodes()
    data = podcast.inspect_first_result(pdict)

    assert isinstance(data, list)
    assert len(data) > 0

    for ep in data:
        title = ep.get("trackName", "").lower()
        assert all(k.lower() in title for k in "fisher") if isinstance("fisher", list) else "fisher".lower() in title

    seen = set()
    for ep in data:
        key = (ep.get("trackName", "").lower(), ep.get("collectionName", "").lower())
        assert key not in seen
        seen.add(key)



if __name__ == "__main__":
    main()
