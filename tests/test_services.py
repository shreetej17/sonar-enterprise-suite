import services

def test_login_success():
    assert services.login_user("admin", "admin123") == "admin"

def test_login_fail():
    assert services.login_user("admin", "x") is None

def test_discount():
    assert services.calculate_discount(10000) == 2000
