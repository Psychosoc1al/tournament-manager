import json
from datetime import date

from marshmallow import Schema, fields, post_load

from participant import Participant
from tournament import Tournament


class TournamentSchema(Schema):
    name = fields.String()
    sport = fields.String()
    tournament_type = fields.String()
    tour_date = fields.Date()
    participants = fields.List(fields.String())

    # noinspection PyUnusedLocal
    @post_load
    def make_tournament(self, data, **kwargs) -> Tournament:
        data['participants'] = [Participant(name) for name in data['participants']]
        return Tournament(**data)

# TODO: save brackets


class MainPage:
    _filename = 'data.json'
    _schema = TournamentSchema(many=True)

    def __init__(self) -> None:
        self._tournaments = []
        self.load_data()

    def load_data(self) -> None:
        with open(self._filename, 'r', encoding='utf-8') as f:
            self._tournaments = self._schema.loads(f.read())

    def save_data(self) -> None:
        with open(self._filename, 'w', encoding='utf-8') as f:
            f.write(
                json.dumps(
                    self._schema.dump(self._tournaments),
                    ensure_ascii=False
                )
            )

    def add_tournament(self, tournament: Tournament) -> None:
        self._tournaments.append(tournament)
        self.save_data()

    def update_tournament(self,
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

    def delete_tournament(self, tournament : Tournament) -> None:
        self._tournaments.remove(tournament)
        self.save_data()

    def get_tournaments(self) -> list[Tournament]:
        return self._tournaments
