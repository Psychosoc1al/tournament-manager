Feature: generate bracket

  Scenario: upper bracket with good count of participants
    Given I create upper bracket
    And I generate 8 participants
    When I generate bracket
    Then I see matches
      |stage|number|name1|name2|
      |0    |0     |0    |1    |
      |0    |1     |2    |3    |
      |0    |2     |4    |5    |
      |0    |3     |6    |7    |
      |1    |0     |???  |???  |
      |1    |1     |???  |???  |
      |2    |0     |???  |???  |

  Scenario: upper bracket with bad count of participants
    Given I create upper bracket
    And I generate 7 participants
    When I generate bracket
    Then I see matches
      |stage|number|name1|name2|
      |0    |0     |0    |1    |
      |0    |1     |2    |3    |
      |0    |2     |4    |5    |
      |0    |3     |6    |???  |
      |1    |0     |???  |???  |
      |1    |1     |???  |6    |
      |2    |0     |???  |???  |

  Scenario: lower bracket with good count of participant
    Given I create lower bracket
    And I generate 8 participants
    When I generate bracket
    Then I see matches
      |stage|number|name1|name2|
      |0    |0     |???  |???  |
      |0    |1     |???  |???  |
      |1    |0     |???  |???  |
      |1    |1     |???  |???  |
      |2    |0     |???  |???  |
      |3    |0     |???  |???  |
      |4    |0     |???  |???  |

  Scenario: lower bracket with bad count of participant
    Given I create lower bracket
    And I generate 7 participants
    When I generate bracket
    Then I see matches
      |stage|number|name1|name2|
      |0    |0     |???  |???  |
      |0    |1     |???  |???  |
      |1    |0     |???  |???  |
      |1    |1     |???  |???  |
      |2    |0     |???  |???  |
      |3    |0     |???  |???  |
      |4    |0     |???  |???  |
