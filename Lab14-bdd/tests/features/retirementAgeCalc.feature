# Exercise: Retirement Behavioral Test (Unit 14)
# Name: Kennedy Komen
# Class: CSC256.0002
# Instructor: K. Poulsen
# Date: 11/26/2021
# This is from unit 13


  Feature: Retirement Behavioral Test
    As a social security administrator,
    I want to see user ages,
    to ascertain when they will receive social security retirement benefits

  Scenario: Get User Ages
    Given user enters correct year of birth
    When birth year is subtracted from current year
    Then retirement age and month is displayed
    And year and month is displayed

    Scenario Outline: Enter year of birth
      Given User is on application
      When User enters year of birth "<birthYear>"
      Then Display "<retirement age>", "<year>", and "<month>"

      Examples: Get birthYear
        | birthYear  | retirement age           | year            | month  |
        | birthYear1 | currentYear - birthYear1 | birthYear1 + 65 | month1 |
        | birthYear2 | currentYear - birthYear2 | birthYear2 + 65 | month2 |
        | birthYear3 | currentYear - birthYear3 | birthYear3 + 65 | month3 |

      Scenario: empty birthYear
        Given User does not enter any year of birth
        When program finds blank input
        Then program loop requests user input

