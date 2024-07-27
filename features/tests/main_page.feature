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


  Scenario: User can add a project through the settings


    Given Open the main page
    And Click Sign in
    Then Input email
    And Input password
    And Click on Continue button
    And Click on Settings option
    When Click on Add a project
    Then Verify the right page opens
    Then Add test information to the input fields
    Then Verify the right information is present in the input field
    And Verify Send an Application button is available and clickable