from pathlib import Path
from pytest import approx

from pytest import fixture

from targer.api import fetch_arguments
from targer.model import (
    ArgumentSentence, ArgumentSentences, ArgumentTag, ArgumentLabel
)


@fixture
def text() -> str:
    return (
        "The alternative vote is advantageous. "
        "The President is directly elected by secret ballot "
        "under the system of the Alternative Vote."
    )


@fixture
def model() -> str:
    return "tag-ibm-fasttext"


@fixture
def api_url() -> str:
    return "https://demo.webis.de/targer-api/"


@fixture
def cache_dir(tmp_path: Path) -> Path:
    return tmp_path


def test_fetch_arguments(
        text: str,
        model: str,
        api_url: str,
        cache_dir: Path,
):
    arguments = fetch_arguments(text, {model}, api_url, cache_dir)

    assert len(arguments) == 1
    assert model in arguments.keys()

    sentences = arguments[model]
    assert isinstance(sentences, ArgumentSentences)
    assert len(sentences) == 2

    sentence1, sentence2 = sentences
    assert isinstance(sentence1, ArgumentSentence)
    assert len(sentence1) == 6
    assert isinstance(sentence2, ArgumentSentence)
    assert len(sentence2) == 16

    sentence1_token2 = sentence1[1]
    assert isinstance(sentence1_token2, ArgumentTag)
    assert isinstance(sentence1_token2.label, ArgumentLabel)
    assert sentence1_token2.label == ArgumentLabel.C_B
    assert sentence1_token2.probability == approx(0.6908648)
    assert sentence1_token2.token == "alternative"

    sentence2_token2 = sentence2[1]
    assert isinstance(sentence2_token2, ArgumentTag)
    assert isinstance(sentence2_token2.label, ArgumentLabel)
    assert sentence2_token2.label == ArgumentLabel.P_B
    assert sentence2_token2.probability == approx(0.9999801)
    assert sentence2_token2.token == "President"
