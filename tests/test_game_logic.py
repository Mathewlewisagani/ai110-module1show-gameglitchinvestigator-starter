from logic_utils import check_guess, HINT_MESSAGES

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# Bug 1: hints were backwards and the secret was sometimes compared as a string.
def test_too_high_hint_says_go_lower():
    outcome = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in HINT_MESSAGES[outcome]

def test_too_low_hint_says_go_higher():
    outcome = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in HINT_MESSAGES[outcome]

def test_string_secret_compares_as_number():
    # Old code compared "100" vs "21" as strings, so 100 was reported "Too Low".
    assert check_guess(100, "21") == "Too High"
    assert check_guess(99, "21") == "Too High"
    assert check_guess(21, "21") == "Win"
