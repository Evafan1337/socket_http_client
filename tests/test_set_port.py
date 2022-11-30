from socket_handler.socket_handler import SocketHandler
import pytest

@pytest.mark.parametrize("correct_port, expected_result", [
    (80, True),
])
def test_set_port_correct(correct_port, expected_result):
    handler = SocketHandler()
    handler.setPort(correct_port)

    definition = handler.getPort() == correct_port
    assert definition == expected_result


@pytest.mark.parametrize("incorrect_port, expected_result", [
    (0, False),
    ("aa", False),
    ("", False),
    (443, False),
    (-1000, False),
    (355, False)
])
def test_set_port_incorrect(incorrect_port, expected_result):
    try:
        handler = SocketHandler()
        handler.setUrl(incorrect_port)
        assert False
    except Exception:
        assert True
