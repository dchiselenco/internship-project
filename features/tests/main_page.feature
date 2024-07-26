# Created by dchis at 7/26/2024
Feature:  Tests for Main page

  Scenario: Verify the user can change the language from the page


    Given Open the main page
    And Click Sign in
    Then Input email
    And Input password
    And Click on Continue button
    When Click on menu
    And Change the language
    Then Verify the language has changed
