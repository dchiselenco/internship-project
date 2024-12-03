# Created by dchis at 11/6/2024
Feature: Tests for Off-plan page
  # Enter feature description here

  Scenario: User can open the off plan page and go through the pagination
    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button
    When Click on Off-plan button
    Then Verify Off-plan page opens
    And Go to the  final Off-plan page using the pagination button
    And Go back to the first Off-plan page using the pagination button


  Scenario: User can filter the off plan products by Unit price range
    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button
    When Click on Off-plan button
    Then Verify Off-plan page opens
    And Click on Filters from header
    And Filter the products by price range from 1200000 to 2000000 AED
    And Click on "Apply Filter" button from header
    And Verify the price in all cards from off-plan pages are inside the range (1200000 - 2000000)


  Scenario:User can see titles and pictures on each product inside the off plan page
    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button
    When Click on Off-plan button
    Then Verify Off-plan page opens
    Then Verify each product on this page contains a title and picture visible