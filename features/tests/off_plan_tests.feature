# Created by dchis at 11/6/2024
Feature: Tests for Off-plan page
  # Enter feature description here

  Scenario: User can open the off plan page and go through the pagination
    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button
    When Click on Off-plan button
    Then Verify Off-plan page opens
    And Go to the  final Off-plan page using the pagination button
    And Go back to the first Off-plan page using the pagination button