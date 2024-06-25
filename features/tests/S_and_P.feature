# Created by dchis at 5/28/2024
Feature: Relly app
  #Reelly is an ecosystem that increases agents` efficiency

  Scenario:User can open Subscription & payments page
    Given Open the main page
    And Click Sign in
    Then Input email
    And Input password
    And Click on Continue button
    And Click on Settings option
    When Click on Subscription & payments option
    Then Verify title Subscription & payments is visible
    And Verify Back button is available
    And Verify  upgrade plan button is available



  Scenario: The user name is visible when log in
    Given Open the main page
    And Click Sign in
    Then Input email
    And Input password
    And Click on Continue button
    And Verify user name is visible



  Scenario: The user can enter the information into the input fields on the registration page
    Given Open the main page
    And Click Sign in
    Then Input email
    And Input password
    And Verify correct username is visible in email field
    And Verify correct password is present in password field