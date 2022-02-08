from hashlib import md5
from pathlib import Path
from typing import Optional, Set, overload, Union

from diskcache import Cache
from requests import Response, post

from targer_api.constants import (
    DEFAULT_TARGER_API_URL, DEFAULT_TARGER_MODEL, DEFAULT_TARGER_MODELS
)
from targer_api.model import ArgumentSentences, ArgumentModelSentences
from targer_api.parse import parse_argument_sentences


@overload
def analyze_text(
        text: str,
        model: str = DEFAULT_TARGER_MODEL,
        api_url: str = DEFAULT_TARGER_API_URL,
        cache_dir: Optional[Path] = None,
) -> ArgumentSentences:
    pass


@overload
def analyze_text(
        text: str,
        models: Set[str],
        api_url: str = DEFAULT_TARGER_API_URL,
        cache_dir: Optional[Path] = None,
) -> ArgumentModelSentences:
    pass


def analyze_text(
        text: str,
        model_or_models: Union[str, Set[str]] = DEFAULT_TARGER_MODEL,
        api_url: str = DEFAULT_TARGER_API_URL,
        cache_dir: Optional[Path] = None,
) -> Union[ArgumentSentences, ArgumentModelSentences]:
    if isinstance(model_or_models, str):
        return _fetch_sentences_single(
            text=text,
            model=model_or_models,
            api_url=api_url,
            cache_dir=cache_dir,
        )
    else:
        return _fetch_sentences_multi(
            text=text,
            models=model_or_models,
            api_url=api_url,
            cache_dir=cache_dir,
        )


def _fetch_sentences_multi(
        text: str,
        models: Set[str] = DEFAULT_TARGER_MODELS,
        api_url: str = DEFAULT_TARGER_API_URL,
        cache_dir: Optional[Path] = None,
) -> ArgumentModelSentences:
    if cache_dir is not None:
        cache_dir.mkdir(parents=True, exist_ok=True)

    arguments: ArgumentModelSentences = {
        model: _fetch_sentences_single(
            text=text,
            model=model,
            api_url=api_url,
            cache_dir=(
                cache_dir / model
                if cache_dir is not None
                else None
            ),
        )
        for model in models
    }
    return arguments


def _fetch_sentences_single(
        text: str,
        model: str = DEFAULT_TARGER_MODEL,
        api_url: str = DEFAULT_TARGER_API_URL,
        cache_dir: Optional[Path] = None,
) -> ArgumentSentences:
    cache_key = md5(text.encode()).hexdigest()
    cache = Cache(str(cache_dir.absolute())) if cache_dir is not None else None

    # Check if the API response is found in the cache.
    if cache is not None and cache_key in cache:
        return cache[cache_key]

    headers = {
        "Accept": "application/json",
        "Content-Type": "text/plain",
    }
    res: Response = post(
        api_url + model,
        headers=headers,
        data=text.encode("utf-8")
    )
    json = res.json()

    argument_sentences = parse_argument_sentences(json)

    # Cache the API response.
    if cache is not None:
        cache[cache_key] = argument_sentences

    return argument_sentences
