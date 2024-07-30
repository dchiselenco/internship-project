# Created by dchis at 7/26/2024
Feature: Feature: Editing on Settings Page

  Scenario: User can go to settings and edit the personal information
    Given Open the main page
    And Click Sign in
    Then Input email
    And Input password
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

  Scenario: User can open the community page
    Given Open the main page
    And Click Sign in
    Then Input email
    And Input password
    And Click on Continue button
    And Click on Settings option
    When Click on Community option
    And Verify the right Community page open
    And Verify “Contact support” button is available and clickable