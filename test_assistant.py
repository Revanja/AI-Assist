from assistant_utils import get_name, get_time, get_date, handle_invalid

def test_name():
    assert "AI Operating System Assistant" in get_name()

def test_time_format():
    time = get_time()
    assert ":" in time   # simple check (e.g., 10:30 AM)

def test_date_format():
    date = get_date()
    assert len(date) > 5  # basic validation

def test_invalid_command():
    assert "cannot perform" in handle_invalid()