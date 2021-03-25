from math import floor


def initial_date_calc(total_days, four_years, years_passed, extra_days):
    if total_days >= four_years:
        years_passed = floor(total_days / four_years)
        years_passed = years_passed * 4
        extra_days = total_days % four_years
    else:
        if total_days < 365:
            years_passed = 0
            extra_days = total_days
        if 365 < total_days < 730:
            years_passed = 1
            extra_days = total_days - 365
        if 730 < total_days < 1096:
            years_passed = 2
            extra_days = total_days - 730
        if 1096 < total_days < four_years:
            years_passed = 3
            extra_days = total_days - 1096
    return years_passed, extra_days


def initial_extra_days_plus_years(extra_days, years_passed):
    if extra_days > 365:
        if extra_days > 365:
            extra_days -= 365
            years_passed += 1
        if extra_days > 365:
            extra_days -= 365
            years_passed += 1
        if extra_days > 366:
            extra_days -= 366
            years_passed += 1
        if extra_days > 365:
            extra_days -= 365
            years_passed += 1

        return extra_days, years_passed

    else:
        return extra_days, years_passed


def extra_day_from_ly(final_year, extra_days):
    # Used https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year#:~:
    # text=Any%20year%20that%20is%20evenly,and%201996%20are%20leap%20years
    # to help calculate missing days. Had to split the URL for PEP8
    first_leap_year = 1972
    while first_leap_year <= final_year:
        if first_leap_year % 100 == 0 and first_leap_year % 400 != 0:
            extra_days += 1
        first_leap_year += 4
    if final_year % 4 == 0 and extra_days >= 366:
        final_year += 1
        extra_days -= 366
    if final_year % 4 != 0 and extra_days >= 365:
        final_year += 1
        extra_days -= 365
    return final_year, extra_days


def final_months_days(extra_days, days_passed, total_days, months_passed, final_year):
    reg_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    months = 0
    if final_year % 4 == 0:
        for d in leap_year:
            days += d
            if extra_days < days:
                months_passed = months
                days_passed = extra_days - (days - d)
                break
            months += 1

    if final_year % 4 != 0:
        for d in reg_year:
            days += d
            if extra_days < days:
                months_passed = months
                days_passed = extra_days - (days - d)
                break
            months += 1

    return days_passed, months_passed
