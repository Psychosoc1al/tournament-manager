import json

from marshmallow import Schema, fields, post_load

from tournament import Tournament


class TournamentSchema(Schema):
    name = fields.String()
    sport = fields.String()
    bracket_type = fields.String()
    tour_date = fields.Date()
    participants = fields.List(fields.String())

    # noinspection PyUnusedLocal
    @post_load
    def make_tournament(self, data, **kwargs):
        return Tournament(**data)


class MainPage:
    _filename = 'data.json'
    _schema = TournamentSchema(many=True)

    def __init__(self):
        self._tournaments = []
        self.load_from_file()

    def load_from_file(self):
        with open(self._filename, 'r', encoding='utf-8') as f:
            self._tournaments = self._schema.loads(f.read())

    def save_to_file(self):
        with open(self._filename, 'w', encoding='utf-8') as f:
            f.write(
                json.dumps(
                    self._schema.dump(self._tournaments),
                    ensure_ascii=False
                )
            )

    def add_tournament(self, tournament):
        self._tournaments.append(tournament)
        self.save_to_file()

    def delete_tournament(self, tournament):
        self._tournaments.remove(tournament)
        self.save_to_file()

    def update_tournament(self, index, new_tournament):
        self._tournaments[index] = new_tournament
        self.save_to_file()

    def get_tournaments(self):
        return self._tournaments
