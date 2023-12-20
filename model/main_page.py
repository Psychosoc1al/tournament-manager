import json
from datetime import date

from marshmallow import Schema, fields, post_load

from model.bracket import Bracket
from model.match import Match
from model.participant import Participant
from model.tournament import Tournament


# noinspection PyUnusedLocal
class ParticipantSchema(Schema):
    name = fields.String()

    @post_load
    def make_participant(self, data, **kwargs) -> Participant:
        return Participant(**data)


# noinspection PyTypeChecker
class MatchSchema(Schema):
    stage = fields.Integer()
    match_number_stage = fields.Integer()
    participant1 = fields.Nested(ParticipantSchema)
    participant2 = fields.Nested(ParticipantSchema)
    score_participant1 = fields.Integer()
    score_participant2 = fields.Integer()

    @post_load
    def make_match(self, data, _) -> Match:
        return Match(**data)


# noinspection PyTypeChecker,PyUnusedLocal
class BracketSchema(Schema):
    bracket_type = fields.Integer()
    matches = fields.List(fields.List(fields.Nested(MatchSchema)))

    @post_load
    def make_bracket(self, data, **kwargs) -> Bracket:
        return Bracket(**data)


# noinspection PyTypeChecker,PyUnusedLocal
class TournamentSchema(Schema):
    name = fields.String()
    sport = fields.String()
    tournament_type = fields.String()
    tour_date = fields.Date()
    participants = fields.List(fields.Nested(ParticipantSchema))
    results = fields.List(
        fields.List(
            fields.List(
                fields.Tuple(
                    (
                        fields.Integer(),
                        fields.Integer(),
                        fields.Integer(),
                        fields.Integer(),
                    )
                )
            )
        )
    )

    @post_load
    def make_tournament(self, data, **kwargs) -> Tournament:
        return Tournament(**data)


class MainPage:
    _filename = "data.json"
    _schema = TournamentSchema(many=True)

    def __init__(
        self, filename: str = _filename, tournaments: list[Tournament] = None
    ) -> None:
        self._filename = filename

        if tournaments is not None:
            self._tournaments = tournaments
        else:
            self._tournaments = []
            self.load_data()

    def load_data(self) -> None:
        with open(self._filename, "r", encoding="utf-8") as f:
            self._tournaments = self._schema.loads(f.read())

    def save_data(self) -> None:
        for tournament in self._tournaments:
            tournament.save_results()

        with open(self._filename, "w", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    self._schema.dump(self._tournaments), ensure_ascii=False, indent=4
                )
            )

    def add_tournament(self, tournament: Tournament) -> None:
        self._tournaments.append(tournament)
        self.save_data()

    def update_tournament(
        self,
        tournament: Tournament,
        name: str,
        sport: str,
        start_date: date,
    ) -> None:
        tournament_id = self._tournaments.index(tournament)
        self._tournaments[tournament_id].name = name
        self._tournaments[tournament_id].sport = sport
        self._tournaments[tournament_id].tour_date = start_date

        self.save_data()

    def delete_tournament(self, tournament: Tournament) -> None:
        self._tournaments.remove(tournament)
        self.save_data()

    def get_tournaments(self) -> list[Tournament]:
        return self._tournaments
