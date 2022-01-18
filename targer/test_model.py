from pytest import fixture

from targer.model import TargerArgumentLabel, TargerArgumentTag


@fixture
def argument_label() -> TargerArgumentLabel:
    return TargerArgumentLabel.C_I


@fixture
def argument_tag(argument_label: TargerArgumentLabel) -> TargerArgumentTag:
    return TargerArgumentTag(argument_label, 0.7, "house")


def test_argument_tag(argument_tag: TargerArgumentTag):
    assert argument_tag.label == TargerArgumentLabel.C_I
    assert argument_tag.probability == 0.7
    assert argument_tag.token == "house"
