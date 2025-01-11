# Created by dchis at 7/26/2024
Feature: Settings test cases
  All testing scenarios for Settings page are located here

  Background:
    Given Open the main page
    And Click Sign in
    Then Input email and password
    And Click on Continue button
    And Click on Settings option

  Scenario: User can go to settings and Edit the personal information
    Then Click on the Edit profile option
    When Enter test data into the name field: Dany C
    Then Enter test data into the phone number field: 832 829 0101
    When Enter test data into the company field: test1
    Then Verify the right information is present in the name input field
    Then Verify the right information is present in the phone number input field
    Then Verify the right information is present in the company input field
    When Check “Save Changes” button is available and clickable
    When Check “Close” button is available and clickable

  Scenario: User can open the Community page
    When Click on Community option
    And Verify the right Community page open
    And Verify “Contact support” button is available and clickable


  Scenario: User can Add a project in Settings page
    When Click on Add a project
    Then Verify the right page opens
    Then Add test information to the input fields
    Then Verify the right information is present in the input field
    And Verify Send an Application button is available and clickable


  Scenario:User can open Subscription & payments page in Settings page
    When Click on Subscription & payments option
    Then Verify that URL of window contains subscription
    Then Verify title Subscription & payments is visible
    And Verify Back button is available
    And Verify  upgrade plan button is available


  Scenario: User can open the Contact us page
    Then Click on "Contact us" button
    Then Verify that URL of window contains contact-us
    And Verify there are at least 4 social media icons
    And Verify “Connect the company” button is available and clickable


  Scenario: User can open User guide page
    Then Click on User Guide button
    Then Verify that URL  contains user-guide
    And Verify all lesson videos contain titles


  Scenario: User can open change password page
    Then Click on Change password option
    And Verify that URL of window contains set-new-password
    And Add some test password to the input fields
    And Verify the “Change password” button is available


  Scenario: User can access Whatsapp and Telegram communities
    Then Click on Support option
    And Switch to Support windows
    And Verify that URL of window contains api.whatsapp.com
    And Go back to Settings page
    And Click on News option
    And Verify that URL of window contains t.me


  Scenario: User can go to settings and see the right number of UI elements
    Then Verify that URL of window contains settings
    And Verify there are 12 options for the settings
    And Verify “Connect the company” button is available and clickable


  Scenario: User can click on verifications settings option and verify the right page opens
  Then Click on the verification option
  And Verify that URL of window contains verification
  Then Verify “upload image” and “Next step” buttons are available

