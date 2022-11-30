from socket_handler.socket_handler import SocketHandler
import pytest

@pytest.mark.parametrize("correct_url, expected_result", [
    ("http://www.airwar.ru/enc/fighter/yak28.html", True),
    ("http://www.airwar.ru/enc/fighter/i211.html", True),
    ("http://www.airwar.ru/enc/fighter/mig21pf.html", True),
    ("http://example.com/", True),
])
def test_set_url_correct(correct_url):

    handler = SocketHandler()
    handler.setUrl(correct_url)

    assert handler.getUrl(correct_url) == correct_url
    #assert "testSetEmpty" == "testSetEmpty"



@pytest.mark.parametrize("incorrect_url", [
    ("", False),
    ("a", False),
    ("www.mp3#.com", False),
    ("http://foufos", False),
    ("www.foufos-.gr", False),
    ("www.mp3#.com", False),
])
def test_set_url_incorrect(incorrect_url):
    assert True
    #assert "testSetInvalidUrl" == "testSetInvalidUrl"


