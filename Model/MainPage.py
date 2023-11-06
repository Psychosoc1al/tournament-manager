import json


class MainPage:
    _filename = 'data.json'

    def __init__(self):
        self._tournaments = []
        self.load_from_file()

    def load_from_file(self):
        with open(self._filename, 'r', encoding='utf-8') as f:
            self._tournaments = json.loads(f.read())

    def save_to_file(self):
        with open(self._filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self._tournaments, indent=4, ensure_ascii=False))

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
