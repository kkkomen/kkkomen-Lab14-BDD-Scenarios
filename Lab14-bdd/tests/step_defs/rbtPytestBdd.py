from datetime import datetime
import behave  
import pytest
from pytest_bdd import scenario, given, when, then

import fullRetirementAgeCalc


@scenario('../features/retirementAgeCalc.feature', 'Get User Ages')
def test_getAge():
    pass


@given("user enters correct year of birth")
def verifyAge():
    return fullRetirementAgeCalc.main()


@when('birth year is subtracted from current year')
def subtract(birth_year):
    current_year = datetime.now().year
    client_age = int(current_year) - birth_year
    return client_age


@then('retirement age and month is displayed')
def age():
    assert subtract > 0 


