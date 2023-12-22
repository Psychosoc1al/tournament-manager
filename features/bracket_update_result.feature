Feature: update results

  Scenario: upper bracket
    Given I create upper bracket
    And I generate 8 participants
    When I generate bracket
    And I update result of stage 0 match 0 1:0
    Then I see matches
      |stage|number|name1|name2|
      |0    |0     |0    |1    |
      |0    |1     |2    |3    |
      |0    |2     |4    |5    |
      |0    |3     |6    |7    |
      |1    |0     |0    |???  |
      |1    |1     |???  |???  |
      |2    |0     |???  |???  |
    When I update result of stage 0 match 1 1:0
    Then I see matches
      |stage|number|name1|name2|
      |0    |0     |0    |1    |
      |0    |1     |2    |3    |
      |0    |2     |4    |5    |
      |0    |3     |6    |7    |
      |1    |0     |0    |2    |
      |1    |1     |???  |???  |
      |2    |0     |???  |???  |
    When I update result of stage 0 match 2 1:0
    Then I see matches
      |stage|number|name1|name2|
      |0    |0     |0    |1    |
      |0    |1     |2    |3    |
      |0    |2     |4    |5    |
      |0    |3     |6    |7    |
      |1    |0     |0    |2    |
      |1    |1     |4    |???  |
      |2    |0     |???  |???  |
    When I update result of stage 0 match 3 1:0
    Then I see matches
      |stage|number|name1|name2|
      |0    |0     |0    |1    |
      |0    |1     |2    |3    |
      |0    |2     |4    |5    |
      |0    |3     |6    |7    |
      |1    |0     |0    |2    |
      |1    |1     |4    |6    |
      |2    |0     |???  |???  |
    When I update result of stage 1 match 0 1:0
    Then I see matches
      |stage|number|name1|name2|
      |0    |0     |0    |1    |
      |0    |1     |2    |3    |
      |0    |2     |4    |5    |
      |0    |3     |6    |7    |
      |1    |0     |0    |2    |
      |1    |1     |4    |6    |
      |2    |0     |0    |???  |
    When I update result of stage 1 match 1 1:0
    Then I see matches
      |stage|number|name1|name2|
      |0    |0     |0    |1    |
      |0    |1     |2    |3    |
      |0    |2     |4    |5    |
      |0    |3     |6    |7    |
      |1    |0     |0    |2    |
      |1    |1     |4    |6    |
      |2    |0     |0    |4    |
    When I update result of stage 2 match 0 1:0
    Then I see matches
      |stage|number|name1|name2|
      |0    |0     |0    |1    |
      |0    |1     |2    |3    |
      |0    |2     |4    |5    |
      |0    |3     |6    |7    |
      |1    |0     |0    |2    |
      |1    |1     |4    |6    |
      |2    |0     |0    |4    |