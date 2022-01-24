from dataclasses import dataclass
from enum import Enum
from math import nan
from typing import List


class ArgumentLabel(Enum):
    C_B = "C-B"
    C_I = "C-I"
    MC_B = "MC-B"
    MC_I = "MC-I"
    P_B = "P-B"
    P_I = "P-I"
    MP_B = "MP-B"
    MP_I = "MP-I"
    O = "O"  # noqa: E741
    B_B = "B-B"
    B_I = "B-I"
    X = "-X-"

    @classmethod
    def from_json(cls, json):
        return cls(str(json))


@dataclass
class ArgumentTag:
    label: ArgumentLabel
    probability: float
    token: str

    @classmethod
    def from_json(cls, json):
        return cls(
            ArgumentLabel.from_json(json["label"]),
            float(json["prob"]) if "prob" in json else nan,
            str(json["token"])
        )


class ArgumentSentence(List[ArgumentTag]):
    @classmethod
    def from_json(cls, json):
        return cls(
            ArgumentTag.from_json(tag)
            for tag in json
        )


class ArgumentSentences(List[ArgumentSentence]):
    @classmethod
    def from_json(cls, json) -> "ArgumentSentences":
        return cls(
            ArgumentSentence.from_json(sentence)
            for sentence in json
        )
