import pytest

def test_always_succeeds():
    assert True


@pytest.mark.xfail
def test_always_fails():
    assert False
