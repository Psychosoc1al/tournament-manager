from Participant import Participant


class Match:
    def __init__(self,
                 stage: int,
                 matchNumberStage: int,
                 Participant1: Participant,
                 Participant2: Participant
                 ) -> None:
        self._stage = stage
        self._matchNumberStage = matchNumberStage
        self._scoreParticipant1 = 0
        self._scoreParticipant2 = 0
        self._Participant1 = Participant1
        self._Participant2 = Participant2

    @property
    def stage(self) -> int:
        return self._stage

    @stage.setter
    def stage(self, value: int) -> None:
        self._stage = value

    @property
    def match_number_stage(self) -> int:
        return self._matchNumberStage

    @match_number_stage.setter
    def match_number_stage(self, value: int) -> None:
        self._matchNumberStage = value

    @property
    def participant1(self) -> Participant:
        return self._Participant1

    @participant1.setter
    def participant1(self, value: Participant) -> None:
        self._Participant1 = value

    @property
    def participant2(self) -> Participant:
        return self._Participant2

    @participant2.setter
    def participant2(self, value: Participant) -> None:
        self._Participant2 = value

    @property
    def score_participant1(self) -> int:
        return self._scoreParticipant1

    @score_participant1.setter
    def score_participant1(self, value: int) -> None:
        self._scoreParticipant1 = value

    @property
    def score_participant2(self) -> int:
        return self._scoreParticipant2

    @score_participant2.setter
    def score_participant2(self, value: int) -> None:
        self._scoreParticipant2 = value

    def move_participant(self) -> None:
        pass  # TODO
