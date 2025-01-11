# Created by dchis at 11/6/2024
Feature: Tests for Off-plan page
  # Enter feature description here


  Background:
    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button
    When Click on Off-plan button

  Scenario: User can open the off plan page and go through the pagination
    Then Verify Off-plan page opens
    And Go to the  final Off-plan page using the pagination button
    And Go back to the first Off-plan page using the pagination button


  Scenario: User can filter the off plan products by Unit price range
    Then Verify Off-plan page opens
    And Click on Filters from header
    And Filter the products by price range from 1200000 to 2000000 AED
    And Click on "Apply Filter" button from header
    And Verify the price in all cards from off-plan pages are inside the range (1200000 - 2000000)


  Scenario:User can see titles and pictures on each product inside the off plan page
    Then Verify Off-plan page opens
    Then Verify each product on this page contains a title and picture visible


  Scenario:User can filter by sale status Out of Stocks
    Then Filter by sale status of “Out of Stock”
    Then Verify each product contains the Out of Stock tag


  Scenario:User can open product detail and see three options of visualization
    Then Click on the first product
    Then Verify the one of the three options of visualization are architecture, interior, lobby

    Then Verify the visualization options are clickable
