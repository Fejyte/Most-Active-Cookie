# importing required modules
import argparse
from datetime import datetime


# create a parser object
parser = argparse.ArgumentParser(description="Parses for arguments of the Most active cookie")

# add arguments
parser.add_argument("filename", help="Store of cookie activity")
parser.add_argument("-d", help="Date of interest")

# parse the arguments from standard input
args = vars(parser.parse_args())


def date_time_converter(arg):
    """
    Function for converting datetime data received as string.
    Also aborts API call if string is in incorrect format
    """
    try:
        return str(datetime.strptime(arg, "%Y-%m-%dT%H:%M:%S").date())
    except ValueError:
        print(arg)
        print("Please ensure your date time is in the format Year-month-dayThour:minute:secondZ")


def get_most_used_cookie(filename, date_of_interest):
    cookie_usage_count = {}
    with open(filename, 'r') as file:
        for line in file:
            cookie_id, datetime_used = line.split(",", 1)[0], line.split(",", 1)[1]
            if cookie_id == 'cookie': continue

            if date_time_converter(datetime_used[:-7]) == date_of_interest:
                if cookie_id in cookie_usage_count.keys():
                    cookie_usage_count[cookie_id] += 1
                else:
                    cookie_usage_count[cookie_id] = 1

    highest_count = max(cookie_usage_count.values())

    for count in cookie_usage_count.keys():
        if cookie_usage_count[count] == highest_count:
            print(count)

    return


get_most_used_cookie(args['filename'], args['d'])