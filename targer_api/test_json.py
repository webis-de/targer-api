from pytest import fixture

from targer_api.model import (
    ArgumentLabel, ArgumentTag, ArgumentSentence, ArgumentSentences
)
from targer_api.parse import (
    parse_argument_label, parse_argument_tag, parse_argument_sentence,
    parse_argument_sentences
)


@fixture
def argument_label() -> ArgumentLabel:
    return ArgumentLabel.C_I


@fixture
def argument_label_json():
    return "C-I"


def test_argument_label_json(
        argument_label: ArgumentLabel,
        argument_label_json,
):
    parsed_argument_label = parse_argument_label(argument_label_json)
    assert isinstance(parsed_argument_label, ArgumentLabel)
    assert parsed_argument_label == argument_label


@fixture
def argument_tag(argument_label: ArgumentLabel) -> ArgumentTag:
    return ArgumentTag(argument_label, 0.7, "house")


@fixture
def argument_tag_json(argument_label_json):
    return {
        "label": argument_label_json,
        "prob": 0.7,
        "token": "house",
    }


def test_argument_tag_json(
        argument_tag: ArgumentTag,
        argument_tag_json
):
    parsed_argument_tag = parse_argument_tag(argument_tag_json)
    assert isinstance(parsed_argument_tag, ArgumentTag)
    assert parsed_argument_tag == argument_tag


@fixture
def argument_sentence(argument_tag: ArgumentTag) -> ArgumentSentence:
    return ArgumentSentence([argument_tag])


@fixture
def argument_sentence_json(argument_tag_json):
    return [argument_tag_json]


def test_argument_sentence_json(
        argument_sentence: ArgumentSentence,
        argument_sentence_json
):
    parsed_argument_sentence = parse_argument_sentence(
        argument_sentence_json
    )
    assert isinstance(parsed_argument_sentence, ArgumentSentence)
    assert parsed_argument_sentence == argument_sentence


@fixture
def argument_sentences(
        argument_sentence: ArgumentSentence
) -> ArgumentSentences:
    return ArgumentSentences([argument_sentence])


@fixture
def argument_sentences_json(argument_sentence_json):
    return [argument_sentence_json]


def test_argument_sentences_json(
        argument_sentences: ArgumentSentences,
        argument_sentences_json
):
    parsed_argument_sentences = parse_argument_sentences(
        argument_sentences_json
    )
    assert isinstance(parsed_argument_sentences, ArgumentSentences)
    assert parsed_argument_sentences == argument_sentences
