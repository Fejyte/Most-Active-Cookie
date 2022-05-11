# Most-Active-Cookie

This program  processes the log file and return the most active
cookie for specified day (defined as teh cookie seen the most times during the day)

This directory consists of the following files:
    
- most_active_cookie.py
  - This is the script which contains the command line program. It consists of several function which 
    receive information from the terminal and return the most active cookie(s)
- test_most_active_cookie.py
  - This contains various tests for the functions written in the "most active cookie file"
- cookie_log.csv
  - This csv file contains the cookie data given in the coding task exercise. It was used for testing the program
- README.md


The command line program is run using the following command:
    
- python most_active_cookie _filename_ -d _date_
  - for example - python most_active_cookie cookie_log.csv -d 2018-12-09

Tests can be run with the Pytest framework using the following command:
-  pytest test_most_active_cookie.py


Note:
- Please ensure the file is a csv file
- For testing, please ensure all aforementioned files are in the same directory