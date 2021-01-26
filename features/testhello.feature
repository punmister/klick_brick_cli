Feature: Testing behaviour for CLI

  Scenario: run a test to check hello
    Given command hello on cli
    When cli is run
    Then it should return 'Hello'