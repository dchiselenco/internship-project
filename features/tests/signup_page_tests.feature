# Created by dchis at 5/28/2024
Feature: Relly app
  #Reelly is an ecosystem that increases agents` efficiency


  Scenario: The user can enter the information into the input fields on the registration page
    Given Open the main page
    And Click Sign in
    Then Input email
    And Input password
    And Verify correct username is visible in email field
    And Verify correct password is present in password field




