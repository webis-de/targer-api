from pytest import fixture

from targer.model import ArgumentLabel, ArgumentTag


@fixture
def argument_label() -> ArgumentLabel:
    return ArgumentLabel.C_I


@fixture
def argument_tag(argument_label: ArgumentLabel) -> ArgumentTag:
    return ArgumentTag(argument_label, 0.7, "house")


def test_argument_tag(argument_tag: ArgumentTag):
    assert argument_tag.label == ArgumentLabel.C_I
    assert argument_tag.probability == 0.7
    assert argument_tag.token == "house"
