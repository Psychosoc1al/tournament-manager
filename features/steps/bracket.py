from behave import use_step_matcher, given, when, then

from model.bracket import Bracket, BracketType
from model.match import Match
from model.participant import Participant

use_step_matcher("re")


@given("I create upper bracket")
def step_impl(context):
    context.bracket = Bracket(BracketType.SINGLE)


@given("I create lower bracket")
def step_impl(context):
    context.bracket = Bracket(BracketType.LOWER)


@given("I generate (?P<count>\\d+) participants")
def step_impl(context, count):
    context.participants = [Participant(str(i)) for i in range(int(count))]


@when("I generate bracket")
def step_impl(context):
    context.bracket.generate_bracket(context.participants)


@then("I see matches")
def step_impl(context):
    for stage, number, name1, name2 in context.table:
        assert (
            context.bracket.matches[int(stage)][int(number)].participant1.name == name1
        )
        assert (
            context.bracket.matches[int(stage)][int(number)].participant2.name == name2
        )


@when(
    "I update result of stage (?P<stage>\\d+) match (?P<number>\\d+) (?P<store1>\\d):(?P<store2>\\d)"
)
def step_impl(context, stage, number, store1, store2):
    context.bracket.update_result(int(stage), int(number), (int(store1), int(store2)))


@then("I see winner is (?P<name>\\d+)")
def step_impl(context, name):
    assert context.bracket.take_winner().name == name


@given(
    "I have match (?P<number>\\d+) on stage (?P<stage>\\d+) (?P<name1>\\d+) - (?P<name2>\\d+) "
    "(?P<store1>\\d):(?P<store2>\\d)"
)
def step_impl(context, number, stage, name1, name2, store1, store2):
    context.match = Match(
        int(stage),
        int(number),
        Participant(name1),
        Participant(name2),
        int(store1),
        int(store2),
    )


@when("I take loser")
def step_impl(context):
    context.bracket.take_loser(context.match)
