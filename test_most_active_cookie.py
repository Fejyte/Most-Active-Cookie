import pytest
from most_active_cookie import read_cli
from most_active_cookie import date_time_converter
from most_active_cookie import read_cookie_data
from most_active_cookie import get_most_used_cookie


#What to test
# Common Cases
# Edge Case
# Boundary Cases
def test_read_cli():
    assert True

def test_date_time_converter():
    assert date_time_converter("2018-12-09T14:19:00") == "2018-12-09"

def test_get_most_used_cookies():
    assert get_most_used_cookie("cookie_log.csv", "2018-12-09") == ["AtY0laUfhglK3lC7"]

def test_get_most_used_cookies():
    assert get_most_used_cookie("cookie_log.csv", "2018-12-08") == ["AtY0laUfhglK3lC7"]