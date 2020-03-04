# Python_VU
Python code I wrote at the Vilnius university.

## Task1.
Write an HTTP log parser in Python.

Sample log file:
https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs

The parser must be able to:
1) Group the logged requests by IP address or HTTP status code(selected by user.)
2) Calculate one of the following (selected by user) for each group:
>1. Request count
>2. Request count percentage of all logged requests
>3. Total number of bytes transferred
3) Print the results in descending order.
4) Optionally limit the number of rows printed (specified by user)
All parameters (including the input file name) should be passed to the parser script from command line. Parameters for (1) and (2) are required, parameter for (4) is optional.

Criteria:
The parser should work (correctly) with any log file of CLF format.
The code should be clean and pythonic. Please do not write Java or C code in Python!
The parser should handle unexpected situations (i.e. empty log file, incorrectly specified command line arguments, etc.) 

Task1's final(submitted) version: 2.0

## Task2.
