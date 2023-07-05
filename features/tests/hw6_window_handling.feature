# Created by eshiavsmith at 7/3/23
Feature: Test window conditions for Terms and Conditions Page


  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon Term page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original
