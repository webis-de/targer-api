from dataclasses import dataclass
from enum import Enum
from math import nan
from typing import List


class TargerArgumentLabel(Enum):
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
class TargerArgumentTag:
    label: TargerArgumentLabel
    probability: float
    token: str

    @classmethod
    def from_json(cls, json):
        return cls(
            TargerArgumentLabel.from_json(json["label"]),
            float(json["prob"]) if "prob" in json else nan,
            str(json["token"])
        )


class TargerArgumentSentence(List[TargerArgumentTag]):
    @classmethod
    def from_json(cls, json):
        return cls(
            TargerArgumentTag.from_json(tag)
            for tag in json
        )


class TargerArgumentSentences(List[TargerArgumentSentence]):
    @classmethod
    def from_json(cls, json) -> "TargerArgumentSentences":
        return cls(
            TargerArgumentSentence.from_json(sentence)
            for sentence in json
        )
