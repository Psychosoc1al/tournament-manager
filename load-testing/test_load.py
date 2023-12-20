import os
import re
import time
from datetime import datetime

import pytest
from pytestqt.qtbot import QtBot

from model.main_page import MainPage
from model.participant import Participant
from model.tournament import Tournament
from views.main_page_view import MainPageView


def get_json_file_path(size: int) -> str:
    size_str = 0
    if 0 < size < 1000:
        size_str = str(size)
    elif size >= 1000:
        size_str = str(size // 1000) + "k"

    return os.path.join(os.path.dirname(__file__), f"data_{size_str}.json")


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
    #     generate_json(2000)

    def test_json_sizes(self, qtbot: QtBot, main_window: MainPageView, timer):
        sizes = [100, 250, 500, 750, 1000, 1250, 1500, 1750]
        print()
        print(*sizes, sep="\n")
        print()

        file_path = (
            os.path.abspath(__file__).split("\\load-testing")[0]
            + "\\model\\main_page.py"
        )
        pattern = r"data.*\.json"

        with open(file_path, "r") as file:
            original_contents = file.read()

        for size in sizes:
            generate_json(size)
            with open(file_path, "r") as file:
                file_contents = file.read()

            updated_contents = re.sub(
                pattern, get_json_file_path(size).replace("\\", "/"), file_contents
            )

            with open(file_path, "w") as file:
                file.write(updated_contents)

            with qtbot.waitExposed(main_window):
                start_time = time.time()
                main_window.show_tournaments(
                    MainPage(get_json_file_path(size))._tournaments
                )

                duration = time.time() - start_time
                qtbot.wait(50)
                print(f"{duration:.2f}".replace(".", ","))

                main_window.tournaments_list_widget.clear()

                with open(file_path, "w") as file:
                    file.write(original_contents)

    @pytest.fixture()
    def main_window(self, qtbot: QtBot):
        window = MainPageView()
        qtbot.addWidget(window)

        yield window
        window.close()
