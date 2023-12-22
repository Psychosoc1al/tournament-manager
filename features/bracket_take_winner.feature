Feature: Take winner

  Scenario: Upper bracket
    Given I create upper bracket
    And I generate 8 participants
    When I generate bracket
    And I update result of stage 0 match 0 1:0
    And I update result of stage 0 match 1 1:0
    And I update result of stage 0 match 2 1:0
    And I update result of stage 0 match 3 1:0
    And I update result of stage 1 match 0 1:0
    And I update result of stage 1 match 1 1:0
    And I update result of stage 2 match 0 1:0
    Then I see winner is 0