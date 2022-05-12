import pytest
from most_active_cookie import get_arguments
from most_active_cookie import date_time_converter
from most_active_cookie import read_cookie_data
from most_active_cookie import get_most_used_cookie


def test_date_time_converter_is_correct():
    assert date_time_converter("2018-12-09T14:19:00") == "2018-12-09"


def test_get_most_used_cookies_correctly_returns_single_cookie():
    assert get_most_used_cookie("cookie_log.csv", "2018-12-09") == ["AtY0laUfhglK3lC7"]


def test_get_most_used_cookies_correctly_returns_multiple_cookies():
    assert get_most_used_cookie("cookie_log.csv", "2018-12-08") == ["SAZuXPGUrfbcn5UA","4sMM2LxV07bPJzwf","fbcn5UAVanZf6UtG"]


def test_read_cookie_data_returns_something():
    assert read_cookie_data("cookie_log.csv")


def test_get_arguments_returns_correct_values():
    assert get_arguments()['filename'] == "test_most_active_cookie.py"


