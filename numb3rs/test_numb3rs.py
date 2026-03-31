from numb3rs import validate


def test_regular_ip():
    assert validate("12.33.45.6") == True
    assert validate("2.3.0.0") == True

def test_big_ip():
    assert validate("275.5.0.22") == False
    assert validate("3.275.0.22") == False
    assert validate("2.5.275.22") == False
    assert validate("5.5.0.275") == False

def test_wrong_ip():
    assert validate("275.5.0.") == False
    assert validate("!^@#") == False
    assert validate("Cat") == False

def test_zero_ip():
    assert validate("000.33.45.6") == False
