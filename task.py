from math import floor
from datetime_helper import extra_day_from_ly, initial_extra_days_plus_years, \
    final_months_days, initial_date_calc


def conv_num(num_str):
    num_store = 0

    # Invalid format handling (incorrect first value)
    if num_str[0] not in "-.0123456789":
        return None

    # Invalid format handling (multiple decimal values)
    if num_str.count(".") > 1:
        return None

    # Parsing positive integers only
    if "." not in num_str:
        if pos_digit_check(num_str):
            num_store = conv_pos_digit(num_str)

        # Parsing negative integers only
        if neg_digit_check(num_str):
            num_str = num_str[1:]
            num_store = -1 * conv_pos_digit(num_str)

    # Parsing positive floats only
    if num_str.count(".") == 1 and num_str.count("-") == 0:
        num_store = pos_float(num_str)

    # Parsing negative floats only
    if num_str.count(".") == 1 and num_str.count("-") == 1:
        num_store = neg_float(num_str)

    return num_store


def pos_digit_check(num_str):
    digits = '0123456789'
    if num_str[0] in digits and num_str[1] != 'x':
        return True

    return False


def neg_digit_check(num_str):
    if num_str[0] == "-":
        return True

    return False


def conv_pos_digit(num_str):
    num_store = 0
    for num in num_str:
        num_store = num_store * 10 + ord(num) - ord('0')

    return num_store


def pos_float(num_str):
    num_store = 0
    frac = 0
    counter = 1
    value = {'0': 0, '1': 1, '2': 2, '3': 3,
             '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    # check if float begins with 0
    if num_str[0] == "0":
        num_str = num_str[1:]

    for num in num_str:
        if num == ".":
            continue
        frac = (frac * 10) + value[num]
        counter *= 10

    num_store = num_store + (frac / counter)

    # check if float ends with a decimal
    if num_str[-1] == ".":
        num_store *= 10 ** len(num_str[:-1])

    # check if float ends with a decimal followed by a 0
    if num_str[-1] == "0" and num_str[-2] == ".":
        num_str = num_str[:-1]
        num_store *= 10 ** len(num_str[:-1])

    return num_store


def neg_float(num_str):
    num_store = 0
    frac = 0
    counter = 1
    value = {'0': 0, '1': 1, '2': 2, '3': 3,
             '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    # check if float begins with 0
    if num_str[1] == "0":
        num_str = num_str[2:]

    for num in num_str[1:]:
        if num == ".":
            continue
        frac = (frac * 10) + value[num]
        counter *= 10

    num_store = (num_store + (frac / counter))

    # check if float ends with a decimal
    if num_str[-1] == ".":
        num_store *= 10 ** (len(num_str[:-1]) - 1)

    # check if float ends with a decimal followed by a 0
    if num_str[-1] == "0" and num_str[-2] == ".":
        num_str = num_str[:-1]
        num_store *= 10 ** (len(num_str[:-1]) - 1)

    num_store *= -1

    return num_store


#######################################################
# # # # # # # # # # # FUNCTION 2 # # # # # # # # # # #
#######################################################

def my_datetime(num_sec):
    seconds_in_day = 86400
    total_days = floor(num_sec / seconds_in_day)

    start_month = 1
    start_day = 1
    start_year = 1970

    years_passed = 0
    months_passed = 0
    days_passed = 0
    extra_days = 0

    # number of days in 4 years because of leap cycle
    four_years = 1461

    years_passed, extra_days = initial_date_calc(total_days, four_years, years_passed, extra_days)

    extra_days, years_passed = initial_extra_days_plus_years(extra_days, years_passed)

    final_year = start_year + years_passed

    final_year, extra_days = extra_day_from_ly(final_year, extra_days)

    days_passed, months_passed = final_months_days(extra_days, days_passed, total_days, months_passed, final_year)

    final_month = start_month + months_passed
    final_day = start_day + days_passed

    return str(final_month).zfill(2) + '-' + str(final_day).zfill(2) + '-' + str(final_year)


#######################################################
# # # # # # # # # # # FUNCTION 3 # # # # # # # # # # #
#######################################################


def conv_endian(num, endian='big'):
    """
    Takes a number and returns the hexadecimal string of the specified endian type;
    returns None if the endian is not 'big' or 'little'
    :param num: a number (positive or negative)
    :param endian: 'big' or 'little'
    :return: hexadecimal string
    """
    if endian != 'big' and endian != 'little':
        return None

    # If the number is negative, store a flag and then convert it to positive
    is_neg = False
    if num < 0:
        is_neg = True
        num = abs(num)

    hex_str = create_hex(num)
    hex_str = fill_hex_string(hex_str)

    # Reverse the order of bits if it's little endian
    if endian == 'little':
        hex_str = little_endian(hex_str)

    # Format the string by adding spaces
    hex_str = space_hex_string(hex_str)

    # If the number was negative, append the negative symbol to the string
    if is_neg:
        hex_str = '-' + hex_str

    return hex_str


def create_hex(num):
    """
    Takes a positive number and returns the hexadecimal string
    """

    # Leverage method 2 outlined here: https://www.wikihow.com/Convert-from-Decimal-to-Hexadecimal

    hexadecimal = ''
    while num >= 16:
        remainder = num % 16
        num = num // 16
        # Convert the remainder to hex & append to hexadecimal string
        hexadecimal = conv_hex(remainder) + hexadecimal
    # Convert the final quotient to hex & append to hexadecimal string
    hexadecimal = conv_hex(num) + hexadecimal

    return hexadecimal


def conv_hex(num):
    """
    Takes a number between 0 and 16 and returns the hexadecimal representation
    """

    if num < 10:
        return str(num)
    if num == 10:
        return 'A'
    if num == 11:
        return 'B'
    if num == 12:
        return 'C'
    if num == 13:
        return 'D'
    if num == 14:
        return 'E'
    if num == 15:
        return 'F'


def fill_hex_string(hex_string):
    """
    Takes a hexadecimal string and will append a 0 if the length is odd
    For example: parameter E91A2 returns 0E91A2
    """
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string

    return hex_string


def little_endian(hex_string):
    """
    Takes a hexadecimal string and returns it in little endian form
    For example: parameter 0E91A2 returns A2910E
    """
    new_string = ''
    for i in range(len(hex_string) - 2, -1, -2):
        new_string = new_string + hex_string[i] + hex_string[i + 1]
    return new_string


def space_hex_string(hex_string):
    """
    Adds a space between bytes
    # For example: parameter 0E91A2 returns 0E 91 A2
    """
    new_string = hex_string[0] + hex_string[1]
    for i in range(2, len(hex_string) - 1, 2):
        new_string = new_string + ' ' + hex_string[i] + hex_string[i + 1]

    return new_string
