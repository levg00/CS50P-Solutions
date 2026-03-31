from jar import Jar


def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    assert jar1.size == 0
    jar2 = Jar(10)
    assert jar2.capacity == 10
    assert jar1.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(1)
    assert jar.size == 10
    jar.withdraw(5)
    assert jar.size == 5
