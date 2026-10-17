def mark_attendance(student_id, status):
    """Simulate recording attendance for a student."""
    if not student_id:
        return False
    if status not in ("Present", "Absent"):
        return False
    return True


def test_mark_present():
    assert mark_attendance("STU101", "Present") is True
    print("PASS: Student marked Present")


def test_mark_absent():
    assert mark_attendance("STU102", "Absent") is True
    print("PASS: Student marked Absent")


def test_empty_student_id():
    assert mark_attendance("", "Present") is False
    print("PASS: Empty student ID is rejected")


def test_invalid_status():
    assert mark_attendance("STU103", "Unknown") is False
    print("PASS: Invalid attendance status is rejected")


if __name__ == "__main__":
    test_mark_present()
    test_mark_absent()
    test_empty_student_id()
    test_invalid_status()
    print("All attendance tests passed.")
