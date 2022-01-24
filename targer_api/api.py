from hashlib import md5
from json import loads
from pathlib import Path
from typing import Dict
from typing import Optional, Set

from requests import Response, post

from targer_api.constants import DEFAULT_TARGER_API_URL, DEFAULT_TARGER_MODELS
from targer_api.model import ArgumentSentences


def fetch_arguments(
        text: str,
        models: Set[str] = DEFAULT_TARGER_MODELS,
        api_url: str = DEFAULT_TARGER_API_URL,
        cache_dir: Optional[Path] = None,
) -> Dict[str, ArgumentSentences]:
    if cache_dir is not None:
        cache_dir.mkdir(parents=True, exist_ok=True)

    arguments: Dict[str, ArgumentSentences] = {
        model: _fetch_sentences(text, model, api_url, cache_dir)
        for model in models
    }
    return arguments


def _fetch_sentences(
        text: str,
        model: str,
        api_url: str = DEFAULT_TARGER_API_URL,
        cache_dir: Optional[Path] = None,
) -> ArgumentSentences:
    content_hash: str = md5(text.encode()).hexdigest()
    cache_file = cache_dir / model / f"{content_hash}.json" \
        if cache_dir is not None \
        else None

    # Check if the API response is found in the cache.
    if cache_file is not None and cache_file.exists() and cache_file.is_file():
        with cache_file.open("r") as file:
            json = loads(file.read())
            return ArgumentSentences.from_json(json)

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

    # Cache the API response.
    if cache_file is not None:
        cache_file.parent.mkdir(exist_ok=True)
        with cache_file.open("wb") as file:
            file.write(res.content)

    return ArgumentSentences.from_json(json)
