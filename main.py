from Bracket import *


# for i in range(4, 17):
#     bracket = Bracket(BracketType.UPPER)
#     bracket.generate_bracket([Participant(str(i)) for i in range(i)])
#     print(*[[(bracket.matches[i][j].participant1.name, bracket.matches[i][j].participant2.name) for j in range(len(bracket.matches[i]))] for i in range(len(bracket.matches))], sep='\n')
# print(*[[bracket.matches[i][j].match_number_stage for j in range(len(bracket.matches[i]))] for i in range(len(bracket.matches))], sep='\n')
bracket = Bracket(BracketType.UPPER)
bracket.generate_bracket([Participant(str(i)) for i in range(7)])
print(*[[(bracket.matches[i][j].participant1.name, bracket.matches[i][j].participant2.name) for j in range(len(bracket.matches[i]))] for i in range(len(bracket.matches))], sep='\n')
bracket.update_result(0, 2, (3, 2))
print(*[[(bracket.matches[i][j].participant1.name, bracket.matches[i][j].participant2.name) for j in range(len(bracket.matches[i]))] for i in range(len(bracket.matches))], sep='\n')
