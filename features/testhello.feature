Feature: Testing behaviour for CLI

  Scenario: run a test to check hello
    Given command hello on cli
    When cli is run
    Then it should return 'Hello'

  Scenario: test onboard --checklist
    Given checklist
    When klickbrick onboard checklist
    Then Create Markdown with all checklist items

  Scenario: test onboard --it-request
    Given it-request
    When klickbrick onboard it-request
    Then open mailto uri

  Scenario: test devtools installation
    Given dev-tools
    When klickbrick onboard --dev-tools or any specific flag
    Then install git, pyenv, poetry or specific tool

  Scenario: test onboard
    Given onboard
    When klick_brick onboard
    Then Run all the options for onboard