import nose.tools
from source.referee_highchair import *

def test_referee_is_an_object():
    referee = Referee()
    assert isinstance(referee, object) == True
