# importing required modules
import argparse
from datetime import datetime


def read_cli():
    # create a parser object
    parser = argparse.ArgumentParser(description="Parses for arguments of the Most active cookie")

    # add arguments
    parser.add_argument("filename", help="Store of cookie activity")
    parser.add_argument("-d", help="Date of interest")

    # parse the arguments from standard input
    arguments = vars(parser.parse_args())

    return arguments


def date_time_converter(arg):
    # Convert argument in one format to a date string
    try:
        return str(datetime.strptime(arg, "%Y-%m-%dT%H:%M:%S").date())
    except ValueError:
        print(arg)
        print("Please ensure your date time is in the format Year-month-dayThour:minute:secondZ")


def read_cookie_data(cookie_file):
    cookie_data = []
    with open(cookie_file, 'r') as file:
        for cookie in file:
            cookie_data.append(cookie)
    return cookie_data


def get_most_used_cookie(filename, date_of_interest):
    cookie_usage_count = {}
    file = read_cookie_data(filename)

    for line in file:
        cookie_id, datetime_used = line.split(",", 1)[0], line.split(",", 1)[1]
        if cookie_id == 'cookie': continue

        if date_time_converter(datetime_used[:-7]) == date_of_interest:
            if cookie_id in cookie_usage_count.keys():
                cookie_usage_count[cookie_id] += 1
            else:
                cookie_usage_count[cookie_id] = 1

    for count in cookie_usage_count.keys():
        if cookie_usage_count[count] == max(cookie_usage_count.values()):
            print(count)

    return cookie_usage_count


if __name__ == "__main__":
    args = read_cli()
    get_most_used_cookie(args['filename'], args['d'])

