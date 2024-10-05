# Created by dchis at 10/4/2024
Feature: Tests for Secondary page
  # Enter feature description here

  Scenario:User can open the Secondary deals page and go through the pagination

    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button
    When Click on Secondary button
    Then Verify that URL of window contains secondary-listings
    And Go to the final page using the pagination button
    And Go back to the first page using the pagination button