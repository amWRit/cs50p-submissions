from lines import get_lines_count

def test_blank_lines():
    assert get_lines_count(["     \n"]) == 0
    assert get_lines_count(["\n"]) == 0
    assert get_lines_count(["       hello\n"]) != 0

def test_comments():
    assert get_lines_count(["# This is a test\n"]) == 0
    assert get_lines_count([" # This is a test\n"]) == 0
    assert get_lines_count(["This is a test\n"]) != 0

def test_valid_lines():
    assert get_lines_count(["print('Hello')\n"]) != 0
    assert get_lines_count(["print('Hello')\n"]) == 1

def test_mix():
    assert get_lines_count(["print('Hello')\n", "     \n", "# This is a test\n"]) == 1