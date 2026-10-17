
def login(username, password):
    """Simulate basic AttendX login validation."""
    if not username or not password:
        return False
    if username == "student1" and password == "attendx123":
        return True
    return False


def test_valid_login():
    assert login("student1", "attendx123") is True
    print("PASS: Valid login")


def test_invalid_password():
    assert login("student1", "wrongpass") is False
    print("PASS: Invalid password is rejected")


def test_empty_username():
    assert login("", "attendx123") is False
    print("PASS: Empty username is rejected")

def test_empty_password():
    assert login("student1", "") is False
    print("PASS: Empty password is rejected")

if __name__ == "__main__":
    test_valid_login()
    test_invalid_password()
    test_empty_username()
    test_empty_password()
    print("All login tests passed.")
