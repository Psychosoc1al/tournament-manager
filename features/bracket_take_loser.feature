Feature: Take loser

  Scenario: Upper bracket
    Given I create lower bracket
    Given I have match 0 on stage 0 0 - 1 1:0
    And I generate 8 participants
    When I generate bracket
    And I take loser
    Then I see matches
      | stage | number | name1 | name2 |
      | 0     | 0      | 1     | ???   |
      | 0     | 1      | ???   | ???   |
      | 1     | 0      | ???   | ???   |
      | 1     | 1      | ???   | ???   |
      | 2     | 0      | ???   | ???   |
      | 3     | 0      | ???   | ???   |
      | 4     | 0      | ???   | ???   |