Feature: Missed Messages Notification
  Assistant can notify user if there are any missed messages when user comes home in the evening

  Scenario: Notification of missed messages in the evening
    Given there are missed messages
     When user has come home
      And it is evening
      And assistant is working
     Then assistant says There are missed messages

  Scenario: No notification of missed messages during day
    Given there are missed messages
     When user has come home
      And it is not evening
      And assistant is working
     Then assistant does not say a thing

  Scenario: No missed messages
    Given there are no missed messages
     When user has come home
      And it is evening
      And assistant is working
     Then assistant does not say a thing