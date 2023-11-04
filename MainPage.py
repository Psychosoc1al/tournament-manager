class MainPage:
    def __init__(self, db_manager):
        self._db_manager = db_manager
        self._tournaments = []

    def add_tournament(self, tournament):
        self._tournaments.append(tournament)
        self._db_manager.save_tournament(tournament)

    def remove_tournament(self, tournament):
        self._tournaments.remove(tournament)
        self._db_manager.delete_tournament(tournament)

    def update_tournament(self, tournament):
        pass

    @property
    def tournaments(self):
        return self._tournaments
