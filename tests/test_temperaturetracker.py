# third party modules
import pytest

# tool modules
from temperaturetracker import TempTracker

def test_temptracker_none():
    TT = TempTracker()
    assert TT.temperatures == {} 
    assert TT.get_max() == None
    assert TT.get_min() == None
    assert TT.get_mean() == None

def test_temptracker_basic():
    TT = TempTracker()
    temperatures = [0, 108, 27, 135]
    for temp in temperatures:
        TT.insert(temp)
    
    assert TT.temperatures == {0:1, 108:1, 27:1, 135:1}
    assert TT.get_max() == 135
    assert TT.get_min() == 0
    assert TT.get_mean() == 67.5

def test_temptracker_multiple_temps():
    TT = TempTracker()
    temperatures = [0, 0, 36, 36, 36, 36, 2, 122, 93, 139, 140, 78, 93]
    for temp in temperatures:
        TT.insert(temp)
    
    assert TT.temperatures == {0:2, 36:4, 2:1, 122:1, 93:2, 139:1, 140:1, 78:1}
    assert TT.get_max() == 140
    assert TT.get_min() == 0
    assert TT.get_mean() == 62.4

def test_temptracker_fail():
    TT = TempTracker()
    with pytest.raises(ValueError):
        TT.insert(141)

