import nose.tools
from source import referee_highchair

def test_referee_is_an_object():
    referee = Referee()
    assert isinstance(referee, object) == True
