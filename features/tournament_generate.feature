Feature: Generate tournament

  Scenario: Single elimination
    Given I generate 8 participants
    And I create new single tournament
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | ???   | ???   |
      | 0       | 1     | 1      | ???   | ???   |
      | 0       | 2     | 0      | ???   | ???   |

  Scenario: Double elimination
    Given I generate 8 participants
    And I create new double tournament
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | ???   | ???   |
      | 0       | 1     | 1      | ???   | ???   |
      | 0       | 2     | 0      | ???   | ???   |
      | 1       | 0     | 0      | ???   | ???   |
      | 1       | 0     | 1      | ???   | ???   |
      | 1       | 1     | 0      | ???   | ???   |
      | 1       | 1     | 1      | ???   | ???   |
      | 1       | 2     | 0      | ???   | ???   |
      | 1       | 3     | 0      | ???   | ???   |
