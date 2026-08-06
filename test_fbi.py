import pytest
from fbi import FBI


def main():
    test_grab_api_returns_dict()
    test_make_dict()


def test_grab_api_returns_dict():
    currFbi = FBI()
    currDict = currFbi.grabAPI()
    assert isinstance(currDict, dict)
    assert len(currDict) > 0
    assert len(currDict) == 58
    for name, description in currDict.items():
        assert isinstance(name, str)
        assert isinstance(description, str)
        assert len(name) > 0
        assert len(description) > 0
        assert "murder" in description.lower() or "homicide" in description.lower()

"""
same test just uses the other function to ensure it
prefroms the same
"""
def test_make_dict():
    currFbi = FBI()
    currDict = currFbi.makeDict()
    assert isinstance(currDict, dict)
    assert len(currDict) > 0
    assert len(currDict) == 58
    for name, description in currDict.items():
        assert isinstance(name, str)
        assert isinstance(description, str)
        assert len(name) > 0
        assert len(description) > 0
        assert "murder" in description.lower() or "homicide" in description.lower()
