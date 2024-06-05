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