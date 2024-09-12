# Created by dchis at 7/26/2024
Feature:  Tests for Main page

   Scenario: The user name is visible when log in
    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button
    And Verify user name is visible



  Scenario: Verify the user can change the language from the page
    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button
    When Click on menu
    And Change the language
    Then Verify the language has changed



  Scenario:The user can click on “Connect the company”

    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button
    And Store original windows
    When Click on Connect the company button
    And Switch to the new tab
    And Verify the right tab opens