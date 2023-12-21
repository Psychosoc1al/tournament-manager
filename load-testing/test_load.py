import os
import time
from datetime import datetime

import pytest
from pytestqt.qtbot import QtBot

from model.main_page import MainPage
from model.participant import Participant
from model.tournament import Tournament
from views.main_page_view import MainPageView


def get_json_file_path(size: int) -> str:
    return os.path.join(os.path.dirname(__file__), f"data_{size}.json")


def generate_json(amount: int):
    tournaments = []
    date = datetime.now()
    participants = [Participant(f"Participant {i}") for i in range(16)]

    for i in range(amount):
        tournament = Tournament(
            f"Tournament {i}", f"Sport {i}", "Single elimination", date, participants
        )

        tournaments.append(tournament)

    json_path = get_json_file_path(amount)
    MainPage(json_path, tournaments).save_data()


class TestLoad:
    @pytest.fixture
    def timer(self, request):
        start_time = time.time()

        yield

        duration = time.time() - start_time
        print(f"\nTest {request.node.name} took {duration:.4f} seconds")

    # def test_generate_json(self, timer):
    #     generate_json(50000)

    def test_json_sizes(self, qtbot: QtBot, main_window: MainPageView, timer):
        sizes = [100, 250, 500, 750, 1000, 1250, 1500, 1750]
        print()
        print(*sizes, sep="\n")
        print()

        for size in sizes:
            generate_json(size)

            with qtbot.waitExposed(main_window):
                start_time = time.time()
                main_window.show_tournaments(
                    MainPage(get_json_file_path(size))._tournaments[:10]
                )

                duration = time.time() - start_time
                # if size == 1500:
                qtbot.wait(5)
                print(f"{duration:.2f}".replace(".", ","))

                main_window.tournaments_list_widget.clear()

    # def test_ijson(self, timer):
    #     for _ in range(50):
    #         with open("data_50k.json", "r") as f:
    #             for item in ijson.items(f, "item.name"):
    #                 print(item)
    #         with open("data_50k.json", "rb") as f:
    #             for item in ijson.items(f, "item.name"):
    #                 print(item)
    #         with open("data_50k.json", "r") as f:
    #             for elem in json.loads(f.read()):
    #                 print(elem["name"])
    #         with open("data_50k.json", "r") as f:
    #             for elem in json.load(f):
    #                 print(elem["name"])

    @pytest.fixture()
    def main_window(self, qtbot: QtBot):
        window = MainPageView()
        qtbot.addWidget(window)

        yield window
        window.close()
