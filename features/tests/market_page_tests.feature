# Created by dchis at 7/30/2024
Feature: Market page test cases
  All testing scenarios for Market page are located here


  Background:
    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button
    When Click on Market button

  Scenario: User can open market tab and go through the pagination

    Then Verify Market page opens
    And Go to the final Market page using the pagination button
    And Go back to the first Market page using the pagination button


