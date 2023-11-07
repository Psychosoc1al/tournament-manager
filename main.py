from Bracket import *
from Tournament import *

# for i in range(4, 17):
#     bracket = Bracket(BracketType.UPPER)
#     bracket.generate_bracket([Participant(str(i)) for i in range(i)])
#     print(*[[(bracket.matches[i][j].participant1.name, bracket.matches[i][j].participant2.name) for j in range(len(bracket.matches[i]))] for i in range(len(bracket.matches))], sep='\n')
# print(*[[bracket.matches[i][j].match_number_stage for j in range(len(bracket.matches[i]))] for i in range(len(bracket.matches))], sep='\n')
tournament = Tournament("Tournament", datetime(2020, 1, 1), [Participant(str(i)) for i in range(8)], TournamentType.DOUBLE)
tournament.create_brackets()

bracket0 = tournament.brackets[0]
print(*[[(bracket0.matches[i][j].participant1.name, bracket0.matches[i][j].participant2.name) for j in range(len(bracket0.matches[i]))] for i in range(len(bracket0.matches))], sep='\n')
print()
bracket1 = tournament.brackets[1]
print(*[[(bracket1.matches[i][j].participant1.name, bracket1.matches[i][j].participant2.name) for j in range(len(bracket1.matches[i]))] for i in range(len(bracket1.matches))], sep='\n')
print()
tournament.update_result(0, 0, (1, 0), BracketType.UPPER)
tournament.update_result(0, 1, (0, 1), BracketType.UPPER)
tournament.update_result(0, 0, (1, 0), BracketType.LOWER)
tournament.update_result(0, 2, (0, 1), BracketType.UPPER)
tournament.update_result(0, 3, (0, 1), BracketType.UPPER)
tournament.update_result(1, 0, (0, 1), BracketType.UPPER)
tournament.update_result(1, 1, (0, 1), BracketType.UPPER)
tournament.update_result(0, 1, (0, 1), BracketType.LOWER)
tournament.update_result(1, 0, (0, 1), BracketType.LOWER)
tournament.update_result(1, 1, (0, 1), BracketType.LOWER)
tournament.update_result(2, 0, (0, 1), BracketType.LOWER)
tournament.update_result(2, 0, (0, 1), BracketType.UPPER)
print(*[[(bracket0.matches[i][j].participant1.name, bracket0.matches[i][j].participant2.name) for j in range(len(bracket0.matches[i]))] for i in range(len(bracket0.matches))], sep='\n')
print()
print(*[[(bracket1.matches[i][j].participant1.name, bracket1.matches[i][j].participant2.name) for j in range(len(bracket1.matches[i]))] for i in range(len(bracket1.matches))], sep='\n')
print()
print(tournament.winner.name)

# Todo: последний матч
