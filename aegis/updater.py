from __future__ import annotations

import json
from dataclasses import dataclass
from urllib.request import urlopen

from aegis.version import __version__


@dataclass(frozen=True)
class UpdateInfo:
    version: str
    download_url: str


def _fetch_update_info(update_url: str) -> UpdateInfo | None:
    if not update_url:
        return None
    with urlopen(update_url, timeout=5) as response:
        payload = json.loads(response.read().decode("utf-8"))
    version = payload.get("version")
    download_url = payload.get("download_url", "")
    if not version:
        return None
    return UpdateInfo(version=version, download_url=download_url)


def _is_newer(current: str, candidate: str) -> bool:
    def to_tuple(value: str) -> tuple[int, ...]:
        return tuple(int(part) for part in value.split(".") if part.isdigit())

    return to_tuple(candidate) > to_tuple(current)


def check_for_updates(update_url: str) -> str | None:
    info = _fetch_update_info(update_url)
    if not info:
        return None
    if _is_newer(__version__, info.version):
        if info.download_url:
            return (
                "Доступно обновление AEGIS. "
                f"Скачайте установщик: {info.download_url}"
            )
        return "Доступно обновление AEGIS. Скачайте новую версию."
    return None
