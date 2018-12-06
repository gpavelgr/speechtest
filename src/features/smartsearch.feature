Feature: Smart Search
  Voice assistant can perform smart search of a term in Wikipedia

  Scenario: User searches for a new term
    Given Assistant is running and listening
    When User says Define gamification
    And Assistant understands input
    Then Assistant searches for term
    And Assistant provides a definion of the term gamification
