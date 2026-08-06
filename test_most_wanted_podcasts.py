import pytest
from most_wanted_podcasts import getFBIList, check_name, search_podcasts

def main():
    test_get_FBI_List()
    test_check_name()

"""
This checks that it properly gets the list from the fbi class
"""
def test_get_FBI_List():
    fbi_list = getFBIList()
    assert isinstance(fbi_list, dict)
    assert len(fbi_list) > 0
    
    for name, description in fbi_list.items():
        assert isinstance(name, str)
        assert isinstance(description, str)
        assert len(name) > 0
        assert len(description) > 0

"""
This checks that it properly checks the name and exits if its invalid
"""
def test_check_name():
    list = getFBIList()
    nameCheck = "ROBERT WILLIAM FISHER"
    new_name = check_name(list, nameCheck)
    assert new_name == "robert william fisher"
    with pytest.raises(SystemExit):
        check_name(list, "invalid name")
    assert check_name(list, "ALVIN SCOTT") == "alvin scott"

"""
Tests that search podcasts is properly retrieving and printing data from applepods.py
"""
def test_search_podcasts():
    results = search_podcasts("robert william fisher")

    assert isinstance(results, list)
    assert len(results) > 0

    for ep in results:
        assert isinstance(ep, dict)
        assert "trackName" in ep
        assert "collectionName" in ep

        full_text = f"{ep.get('trackName', '')} {ep.get('collectionName', '')}".lower()
        assert "robert" in full_text
        assert "fisher" in full_text

    seen = set()
    for ep in results:
        key = (ep.get("trackName", "").lower(), ep.get("collectionName", "").lower())
        assert key not in seen
        seen.add(key)




if __name__ == "__main__":
    main()
