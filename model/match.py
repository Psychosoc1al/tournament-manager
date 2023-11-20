from model.participant import Participant


class Match:
    def __init__(self,
                 stage: int,
                 match_number_stage: int,
                 participant1: Participant,
                 participant2: Participant
                 ) -> None:
        self.stage = stage
        self.match_number_stage = match_number_stage
        self.score_participant1 = 0
        self.score_participant2 = 0
        self.participant1 = participant1
        self.participant2 = participant2

    @property
    def stage(self) -> int:
        return self._stage

    @stage.setter
    def stage(self, value: int) -> None:
        self._stage = value

    @property
    def match_number_stage(self) -> int:
        return self._match_number_stage

    @match_number_stage.setter
    def match_number_stage(self, value: int) -> None:
        self._match_number_stage = value

    @property
    def participant1(self) -> Participant:
        return self._participant1

    @participant1.setter
    def participant1(self, value: Participant) -> None:
        self._participant1 = value

    @property
    def participant2(self) -> Participant:
        return self._participant2

    @participant2.setter
    def participant2(self, value: Participant) -> None:
        self._participant2 = value

    @property
    def score_participant1(self) -> int:
        return self._score_participant1

    @score_participant1.setter
    def score_participant1(self, value: int) -> None:
        self._score_participant1 = value

    @property
    def score_participant2(self) -> int:
        return self._score_participant2

    @score_participant2.setter
    def score_participant2(self, value: int) -> None:
        self._score_participant2 = value

    def __str__(self) -> str:
        return (str(self.participant1) + ' ' + str(self.score_participant1) + ' vs ' +
                str(self.score_participant2) + ' ' + str(self.participant2))
