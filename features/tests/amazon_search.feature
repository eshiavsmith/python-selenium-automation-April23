# Created by eshiavsmith at 5/18/23
Feature: Amazon Search Tests

  Scenario: User can search on Amazon
    Given Open Amazon main page
    Wheen Search for table
    Then Verify search results shown