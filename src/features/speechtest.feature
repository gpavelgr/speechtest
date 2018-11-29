Feature: Speech test
  Testing speech recognition

  Scenario: Saying hello
    Given The assistant is listening
     When user says word Hello
      And assistant recognizes command
     Then assistant says Hello

