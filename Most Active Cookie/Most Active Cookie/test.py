import pytest
from most_active_cookie import read_cli
from most_active_cookie import date_time_converter
from most_active_cookie import read_cookie_data
from most_active_cookie import get_most_used_cookie


def just_check():
    assert True



'''def datetime_returns_correct_format():
    assert date_time_converter("2018-12-09T14:19:00") == "2018-12-09", "Incorrect number of arguments"'''


'''def ensure_correct_total_count():
    filename = "cookie_log.csv"
    date_of_interest = "2018-12-08"
    assert sum(get_most_used_cookie(filename, date_of_interest)) == len(read_cookie_data(filename))
'''

