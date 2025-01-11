# Created by dchis at 7/26/2024
Feature:  Tests for Main page


  Background:
    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button

  Scenario: The user name is visible when log in
    Then Verify user name is visible


  Scenario: Verify the user can change the language from the page
    When Click on menu
    And Change the language
    Then Verify the language has changed


  Scenario:The user can click on “Connect the company”
    Then Store original windows
    When Click on Connect the company button
    And Switch to the new tab
    And Verify the right tab opens


