import math_lib as math
import pytest
import sys


@pytest.mark.parametrize('a, b, expected_output', [(10, 5, 50), (-1, 1, -1), (-1, -1, 1)])
def test_multiply(a, b, expected_output):
    assert (math.multiply(a, b) == expected_output)


@pytest.mark.parametrize('a, b, expected_output', [(10, 5, 15), (-1, 1, 0), (-1, -1, -2)])
def test_add(a, b, expected_output):
    assert (math.add(a, b) == expected_output)


def test_subtract():
    assert (math.subtract(15, 5) == 10)
    assert (math.subtract(-1, 1) == -2)
    assert (math.subtract(-1, -1) == 0)
    assert (math.subtract(-1, 1) == -2)


def test_divide():
    assert (math.divide(10, 5) == 2)
    assert (math.divide(-1, 1) == -1)
    assert (math.divide(-1, -1) == 1)
    assert (math.divide(0, 1) == 0)
    with pytest.raises(ValueError):
        math.divide(10, 0)


@pytest.mark.skip(reason='A dummy test method')
def test_dummy():
    assert True


@pytest.mark.skipif(sys.version_info > (3,  5), reason='Dont run in python version > 3.5. This python version is:{}'.format(sys.version_info))
def test_dummy2():
    assert True


@pytest.mark.windows
def test_dummy_win1():
    assert True


@pytest.mark.windows
def test_dummy_win2():
    assert True


@pytest.mark.mac
def test_dummy_mac1():
    assert True


@pytest.mark.mac
def test_dummy_mac2():
    assert True
