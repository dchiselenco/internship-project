# Created by dchis at 10/4/2024
Feature: Tests for Secondary page
  # Enter feature description here

  Background:
    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button
    When Click on Secondary button
    Then Verify that URL of window contains secondary-listings

  Scenario:User can open the Secondary deals page and go through the pagination
    Then Go to the final page using the pagination button
    And Go back to the first page using the pagination button


  Scenario: User can filter the Secondary deals by “want to sell” option
    Then Click on Filters
    And Filter the products by "Want to sell"
    And Click on "Apply Filter" button
    And Verify all cards have “for sale” tag


  Scenario: User can filter the Secondary deals by “want to buy” option
    Then Click on Filters
    And Filter the products by “Want to buy”
    And Click on "Apply Filter" button
    And Verify all cards have “Want to buy” tag


  Scenario: User can filter the Secondary deals by Unit price range
    Then Click on Filters
    And Filter the products by price range from 1200000 to 2000000 AED
    And Click on "Apply Filter" button
    And Verify the price in all cards is inside the range (1200000 - 2000000)
