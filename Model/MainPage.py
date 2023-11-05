import json


class MainPage:
    def __init__(self, filename):
        self._tournaments = []
        self._filename = filename
        self.load_from_file()

    def load_from_file(self):
        with open(self._filename, 'r') as f:
            self._tournaments = json.load(f)

    def save_to_file(self):
        with open(self._filename, 'w') as f:
            json.dump(self._tournaments, f)

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
