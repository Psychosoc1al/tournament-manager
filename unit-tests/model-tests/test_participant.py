import pytest
from participant import Participant


class TestParticipant:

    def test_name_getter(self):
        participant = Participant("Name")
        name = participant.name
        assert "Name" == name

    def test_name_setter(self):
        participant = Participant()
        participant.name = "Name"
        assert "Name" == participant.name
