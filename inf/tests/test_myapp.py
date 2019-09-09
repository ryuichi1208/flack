from src.myapp import Foo
import pytest
import unittest
import requests


@pytest.mark.parametrize(
    "x, y, z", [
        (1, 1, 1),
        (2, 2, 4),
        (3, 3, 9),
        (4, 4, 16),
        (100, 100, 10000)
    ]
)
def test_multiplication(x, y, z):
    assert Foo.multiplication(x, y) == z

@pytest.mark.parametrize(
    "x, y, z", [
        (1, 1, 1),
        (4, 2, 2),
        (16, 4, 4),
        (10000, 10000, 1)
    ]
)
def test_division(x, y, z):
    assert Foo.division(x, y) == z

def test_division_raise():
    with pytest.raises(ZeroDivisionError):
        Foo.division(1, 0)

    with pytest.raises(TypeError):
        Foo.division("a", 4)

class HttpTest(unittest.TestCase):

    def test_http_request(self):
        assert Foo.http_request("https://www.google.com") == 200

    def test_http_request_redirect(self):
        with pytest.raises(requests.exceptions.ConnectionError):
            Foo.http_request("https://localhost:9999") == 404
