from datetime import date
from unittest.mock import Mock

import pytest

from model.main_page import MainPage
from model.tournament import Tournament


class TestMainPage:
    @pytest.fixture
    def mock_tournament(self, monkeypatch):
        tournament_mock = Mock(spec=Tournament)
        monkeypatch.setattr("model.main_page.Tournament", tournament_mock)
        return tournament_mock

    @pytest.fixture
    def main_page(self):
        main_page = MainPage()
        return main_page

    def test_get_tournaments(self, main_page, mock_tournament):
        mock_tournament_instance = mock_tournament.return_value
        main_page._tournaments = [mock_tournament_instance]

        tournaments = main_page.get_tournaments()

        assert len(tournaments) == 1
        assert tournaments[0] == mock_tournament_instance

    def test_add_tournament(self, main_page, mock_tournament, monkeypatch):
        mock_tournament_instance = mock_tournament.return_value
        mock_save_data = Mock()
        monkeypatch.setattr("model.main_page.MainPage.save_data", mock_save_data)

        main_page.add_tournament(mock_tournament_instance)

        assert len(main_page._tournaments) == 1
        assert main_page._tournaments[0] == mock_tournament_instance
        mock_save_data.assert_called_once()

    def test_update_tournament(self, main_page, mock_tournament, monkeypatch):
        mock_tournament_instance = mock_tournament.return_value
        mock_tournament_instance.name = "old_name"
        mock_save_data = Mock()
        monkeypatch.setattr("model.main_page.MainPage.save_data", mock_save_data)
        main_page._tournaments = [mock_tournament_instance]

        main_page.update_tournament(
            mock_tournament_instance, "new_name", "sport", date(2023, 1, 1)
        )

        assert mock_tournament_instance.name == "new_name"
        assert mock_tournament_instance.sport == "sport"
        assert mock_tournament_instance.tour_date == date(2023, 1, 1)
        mock_save_data.assert_called_once()

    def test_delete_tournament(self, main_page, mock_tournament, monkeypatch):
        mock_tournament_instance = mock_tournament.return_value
        mock_save_data = Mock()
        monkeypatch.setattr("model.main_page.MainPage.save_data", mock_save_data)
        main_page._tournaments = [mock_tournament_instance]

        main_page.delete_tournament(mock_tournament_instance)

        assert len(main_page._tournaments) == 0
        mock_save_data.assert_called_once()
