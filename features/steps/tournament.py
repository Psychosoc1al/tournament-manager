from datetime import date

from behave import use_step_matcher, given, when, then

from bracket import BracketType
from model.tournament import Tournament, TournamentType

use_step_matcher("re")


@given("I create new single tournament")
def step_impl(context):
    context.tournament = Tournament(
        "name", "sport", TournamentType.SINGLE, date.today(), context.participants
    )


@then("I see tournament with matches")
def step_impl(context):
    for bracket, stage, number, name1, name2 in context.table:
        assert (
            context.tournament.brackets[int(bracket)]
            .matches[int(stage)][int(number)]
            .participant1.name
            == name1
        )
        assert (
            context.tournament.brackets[int(bracket)]
            .matches[int(stage)][int(number)]
            .participant2.name
            == name2
        )


@given("I create new double tournament")
def step_impl(context):
    context.tournament = Tournament(
        "name", "sport", TournamentType.DOUBLE, date.today(), context.participants
    )


@when(
    "I update result (?P<bracket>\\d+) (?P<stage>\\d+) (?P<number>\\d+) on (?P<score1>\\d+):(?P<score2>\\d)"
)
def step_impl(context, bracket, stage, number, score1, score2):
    if bracket == "1":
        context.tournament.update_result(
            int(stage), int(number), (int(score1), int(score2)), BracketType.LOWER
        )
    else:
        context.tournament.update_result(
            int(stage), int(number), (int(score1), int(score2))
        )


@then("I have winner (?P<name>.*)")
def step_impl(context, name):
    assert context.tournament.winner.name == name
