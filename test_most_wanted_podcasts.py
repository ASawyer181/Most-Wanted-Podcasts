import pytest
from test_most_wanted_podcasts import getFBIList
from test_most_wanted_podcasts import check_name
from test_most_wanted_podcasts import search_podcasts

def main():
    test_get_FBI_List()
    test_check_name()

"""
This checks that it properly gets the list from the fbi class
"""
def test_get_FBI_List():
    list = getFBIList()
    assert len(list) == 58
    assert len(list) > 0
    first_name, first_des = next(iter(list.items()))
    assert first_name == "EDGARDO LUIS PEREZ"
    assert first_des == "Unlawful Flight to Avoid Prosecution - Felony Murder"

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
    dict1 = results[0]
    assert dict1.get("trackName") == "The Man Who Blew Up His House - ROBERT FISHER"
    assert dict1.get("collectionName") == "Crime at Bedtime"
    dict1 = results[1]
    assert dict1.get("trackName") == "Robert William Fisher"
    assert dict1.get("collectionName") == "Crime, Phenomenon & Beyond"




if __name__ == "__main__":
    main()
