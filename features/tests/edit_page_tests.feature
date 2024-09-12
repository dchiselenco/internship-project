# Created by dchis at 7/30/2024
Feature: Edit test cases
  All testing scenarios for Edit page are located here

  Scenario: User can go to  edit to verify personal information

    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button
    And Click on Settings option
    Then Click on the Edit profile option
    When Enter test data into the name field: Dany C
    Then Enter test data into the phone number field: 832 829 0101
    When Enter test data into the company field: test1
    Then Verify the right information is present in the name input field
    Then Verify the right information is present in the phone number input field
    Then Verify the right information is present in the company input field
    When Check “Save Changes” button is available and clickable
    When Check “Close” button is available and clickable