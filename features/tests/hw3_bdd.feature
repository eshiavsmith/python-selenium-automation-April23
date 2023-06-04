
Feature: Amazon Search
  Scenario: Verify sign-in
      Given Open Amazon page
      When Click Orders button
      Then Verify Sign-In Page opened


  Scenario: Verify cart is empty
      Given Open Amazon page
      When Click Cart button
      Then Verify Amazon Cart Empty