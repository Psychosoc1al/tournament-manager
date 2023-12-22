Feature: Eliminations

  Scenario: Single elimination
    Given I generate 8 participants
    And I create new single tournament
    When I update result 0 0 0 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | ???   |
      | 0       | 1     | 1      | ???   | ???   |
      | 0       | 2     | 0      | ???   | ???   |
    When I update result 0 0 1 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | ???   | ???   |
      | 0       | 2     | 0      | ???   | ???   |
    When I update result 0 0 2 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | ???   |
      | 0       | 2     | 0      | ???   | ???   |
    When I update result 0 0 3 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | ???   | ???   |
    When I update result 0 1 0 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | 0     | ???   |
    When I update result 0 1 1 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | 0     | 4     |
    When I update result 0 2 0 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | 0     | 4     |

  Scenario: Double elimination
    Given I generate 8 participants
    And I create new double tournament
    When I update result 0 0 0 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | ???   |
      | 0       | 1     | 1      | ???   | ???   |
      | 0       | 2     | 0      | ???   | ???   |
      | 1       | 0     | 0      | 1     | ???   |
      | 1       | 0     | 1      | ???   | ???   |
      | 1       | 1     | 0      | ???   | ???   |
      | 1       | 1     | 1      | ???   | ???   |
      | 1       | 2     | 0      | ???   | ???   |
      | 1       | 3     | 0      | ???   | ???   |
      | 1       | 4     | 0      | ???   | ???   |
    When I update result 0 0 1 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | ???   | ???   |
      | 0       | 2     | 0      | ???   | ???   |
      | 1       | 0     | 0      | 1     | 3     |
      | 1       | 0     | 1      | ???   | ???   |
      | 1       | 1     | 0      | ???   | ???   |
      | 1       | 1     | 1      | ???   | ???   |
      | 1       | 2     | 0      | ???   | ???   |
      | 1       | 3     | 0      | ???   | ???   |
      | 1       | 4     | 0      | ???   | ???   |
    When I update result 0 0 2 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | ???   |
      | 0       | 2     | 0      | ???   | ???   |
      | 1       | 0     | 0      | 1     | 3     |
      | 1       | 0     | 1      | 5     | ???   |
      | 1       | 1     | 0      | ???   | ???   |
      | 1       | 1     | 1      | ???   | ???   |
      | 1       | 2     | 0      | ???   | ???   |
      | 1       | 3     | 0      | ???   | ???   |
      | 1       | 4     | 0      | ???   | ???   |
    When I update result 0 0 3 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | ???   | ???   |
      | 1       | 0     | 0      | 1     | 3     |
      | 1       | 0     | 1      | 5     | 7     |
      | 1       | 1     | 0      | ???   | ???   |
      | 1       | 1     | 1      | ???   | ???   |
      | 1       | 2     | 0      | ???   | ???   |
      | 1       | 3     | 0      | ???   | ???   |
      | 1       | 4     | 0      | ???   | ???   |
    When I update result 0 1 0 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | 0     | ???   |
      | 1       | 0     | 0      | 1     | 3     |
      | 1       | 0     | 1      | 5     | 7     |
      | 1       | 1     | 0      | ???   | ???   |
      | 1       | 1     | 1      | 2     | ???   |
      | 1       | 2     | 0      | ???   | ???   |
      | 1       | 3     | 0      | ???   | ???   |
      | 1       | 4     | 0      | ???   | ???   |
    When I update result 0 1 1 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | 0     | 4     |
      | 1       | 0     | 0      | 1     | 3     |
      | 1       | 0     | 1      | 5     | 7     |
      | 1       | 1     | 0      | 6     | ???   |
      | 1       | 1     | 1      | 2     | ???   |
      | 1       | 2     | 0      | ???   | ???   |
      | 1       | 3     | 0      | ???   | ???   |
      | 1       | 4     | 0      | ???   | ???   |
    When I update result 0 2 0 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | 0     | 4     |
      | 1       | 0     | 0      | 1     | 3     |
      | 1       | 0     | 1      | 5     | 7     |
      | 1       | 1     | 0      | 6     | ???   |
      | 1       | 1     | 1      | 2     | ???   |
      | 1       | 2     | 0      | ???   | ???   |
      | 1       | 3     | 0      | 4     | ???   |
      | 1       | 4     | 0      | ???   | 0     |
    When I update result 1 0 0 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | 0     | 4     |
      | 1       | 0     | 0      | 1     | 3     |
      | 1       | 0     | 1      | 5     | 7     |
      | 1       | 1     | 0      | 6     | 1     |
      | 1       | 1     | 1      | 2     | ???   |
      | 1       | 2     | 0      | ???   | ???   |
      | 1       | 3     | 0      | 4     | ???   |
      | 1       | 4     | 0      | ???   | 0     |
    When I update result 1 0 1 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | 0     | 4     |
      | 1       | 0     | 0      | 1     | 3     |
      | 1       | 0     | 1      | 5     | 7     |
      | 1       | 1     | 0      | 6     | 1     |
      | 1       | 1     | 1      | 2     | 5     |
      | 1       | 2     | 0      | ???   | ???   |
      | 1       | 3     | 0      | 4     | ???   |
      | 1       | 4     | 0      | ???   | 0     |
    When I update result 1 1 0 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | 0     | 4     |
      | 1       | 0     | 0      | 1     | 3     |
      | 1       | 0     | 1      | 5     | 7     |
      | 1       | 1     | 0      | 6     | 1     |
      | 1       | 1     | 1      | 2     | 5     |
      | 1       | 2     | 0      | 6     | ???   |
      | 1       | 3     | 0      | 4     | ???   |
      | 1       | 4     | 0      | ???   | 0     |
    When I update result 1 1 1 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | 0     | 4     |
      | 1       | 0     | 0      | 1     | 3     |
      | 1       | 0     | 1      | 5     | 7     |
      | 1       | 1     | 0      | 6     | 1     |
      | 1       | 1     | 1      | 2     | 5     |
      | 1       | 2     | 0      | 6     | 2     |
      | 1       | 3     | 0      | 4     | ???   |
      | 1       | 4     | 0      | ???   | 0     |
    When I update result 1 2 0 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | 0     | 4     |
      | 1       | 0     | 0      | 1     | 3     |
      | 1       | 0     | 1      | 5     | 7     |
      | 1       | 1     | 0      | 6     | 1     |
      | 1       | 1     | 1      | 2     | 5     |
      | 1       | 2     | 0      | 6     | 2     |
      | 1       | 3     | 0      | 4     | 6     |
      | 1       | 4     | 0      | ???   | 0     |
    When I update result 1 3 0 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | 0     | 4     |
      | 1       | 0     | 0      | 1     | 3     |
      | 1       | 0     | 1      | 5     | 7     |
      | 1       | 1     | 0      | 6     | 1     |
      | 1       | 1     | 1      | 2     | 5     |
      | 1       | 2     | 0      | 6     | 2     |
      | 1       | 3     | 0      | 4     | 6     |
      | 1       | 4     | 0      | 4     | 0     |
    When I update result 1 4 0 on 1:0
    Then I see tournament with matches
      | bracket | stage | number | name1 | name2 |
      | 0       | 0     | 0      | 0     | 1     |
      | 0       | 0     | 1      | 2     | 3     |
      | 0       | 0     | 2      | 4     | 5     |
      | 0       | 0     | 3      | 6     | 7     |
      | 0       | 1     | 0      | 0     | 2     |
      | 0       | 1     | 1      | 4     | 6     |
      | 0       | 2     | 0      | 0     | 4     |
      | 1       | 0     | 0      | 1     | 3     |
      | 1       | 0     | 1      | 5     | 7     |
      | 1       | 1     | 0      | 6     | 1     |
      | 1       | 1     | 1      | 2     | 5     |
      | 1       | 2     | 0      | 6     | 2     |
      | 1       | 3     | 0      | 4     | 6     |
      | 1       | 4     | 0      | 4     | 0     |
    And I have winner 4