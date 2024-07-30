# Created by dchis at 7/12/2024
Feature: Relly app
  The user can click on “Connect the company” on the left side of the main page

  Scenario:The user can click on “Connect the company”
    Given Open the main page
    And Click Sign in
    Then Input email
    And Input password
    And Click on Continue button
    And Store original windows
    When Click on Connect the company button
    And Switch to the new tab
    And Verify the right tab opens

