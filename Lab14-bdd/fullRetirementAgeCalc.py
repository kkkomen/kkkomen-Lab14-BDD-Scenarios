# Exercise: Full Retirement Age
# For unit 14
# Name: Kennedy Komen
# Class: CSC256.0002 (Taken from Unit 1)
# Instructor: K. Poulsen
# Date: 11/28/2021

import calendar
from _datetime import datetime
import sys


def main():
    print("Social Security Full Retirement Age Calculator")

    while True:
        # asks the user for a birth year and month,
        client_year = (input("Enter your year of Birth or Enter to exit: "))

        if client_year == "":
            sys.exit("Process finished with exit code 0")

        client_year = int(client_year)
        current_year = datetime.now().year  # gets the current year

        while client_year < 1900 or client_year > int(current_year):   # loop tests whether year is below 1900 or above current year
            print("Invalid year!")
            client_year = (input("Enter your year of Birth or press Enter to exit: "))
            int(client_year)
            current_year = datetime.now().year

        else:
            client_month = int(input("Enter your month of birth: "))

            # Loop to test client year and month and
            # displays the age (with additional months) for obtaining full SSA benefits
            if client_year <= 1942:
                client_month += 8
                if client_month > 12:   # adds year if total exceeds 12 months
                    client_year += 1
                    client_month -= 12
                retirement_age = client_year + 65  # returns retirement age
                word_month = calendar.month_name[client_month]   # returns month
                print("Your retirement age is 65 years and 8 months")
                print("this will be in ", word_month, " of ", retirement_age)
                print()

            elif 1943 <= client_year <= 1954:
                retirement_age = client_year + 66
                word_month = calendar.month_name[client_month]
                print("Your retirement age is 66 years and 0 months")
                print("this will be in ", word_month, " of ", retirement_age)
                print()

            elif client_year == 1955:
                client_month += 2
                if client_month > 12:
                    client_year += 1
                    client_month -= 12
                retirement_age = client_year + 66
                word_month = calendar.month_name[client_month]
                print("Your retirement age is 66 years and 2 months")
                print("this will be in ", word_month, " of ", retirement_age)
                print()

            elif client_year == 1956:
                client_month += 4
                if client_month > 12:
                    client_year += 1
                    client_month -= 12
                retirement_age = client_year + 66
                word_month = calendar.month_name[client_month]
                print("Your retirement age is 66 years and 4 months")
                print("this will be in ", word_month, " of ", retirement_age)
                print()

            elif client_year == 1957:
                client_month += 6
                if client_month > 12:
                    client_year += 1
                    client_month -= 12
                retirement_age = client_year + 66
                word_month = calendar.month_name[client_month]
                print("Your retirement age is 66 years and 6 months")
                print("this will be in ", word_month, " of ", retirement_age)
                print()

            elif client_year == 1958:
                client_month += 8
                if client_month > 12:
                    client_year += 1
                    client_month -= 12
                retirement_age = client_year + 66
                word_month = calendar.month_name[client_month]
                print("Your retirement age is 66 years and 8 months")
                print("this will be in ", word_month, " of ", retirement_age)
                print()

            elif client_year == 1959:
                client_month += 10
                if client_month > 12:
                    client_year += 1
                    client_month -= 12
                retirement_age = client_year + 66
                word_month = calendar.month_name[client_month]
                print("Your retirement age is 66 years and 10 months")
                print("this will be in ", word_month, " of ", retirement_age)
                print()

            elif client_year >= 1960:
                retirement_age = client_year + 67
                word_month = calendar.month_name[client_month]
                print("Your retirement age is 67 years")
                print("this will be in ", word_month, " of ", retirement_age)
                print()


main()  # invokes main
