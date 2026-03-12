# -*- coding: utf-8 -*-
"""
@Time    : 2026/3/12 1:26
@Author  : Minghe Liu
@File    : text_api.py
@Description : 
"""
import json
import os
import urllib.parse
import requests
from dotenv import load_dotenv

BASE_URL = "https://api.clashofclans.com/v1"


def build_player_url(player_tag: str) -> str:
    return f"{BASE_URL}/players/{urllib.parse.quote(player_tag)}"


def get_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def fetch_player(player_tag: str, token: str) -> dict:
    url = build_player_url(player_tag)
    resp = requests.get(url=url, headers=get_headers(token), timeout=10)
    resp.raise_for_status()
    return resp.json()


def dump_date(d: dict, filename: str = "player_raw.json") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("COC_API_TOKEN")
    player_tag = os.getenv("COC_PLAYER_TAG")

    if not token:
        raise RuntimeError("COC_API_TOKEN is missing")
    if not player_tag:
        raise RuntimeError("COC_PLAYER_TAG is missing")

    data = fetch_player(player_tag, token)
    dump_date(data)
    print("townHallLevel:", data.get("townHallLevel"))
    print("heroes:", [f'{h["name"]}:{h["level"]}' for h in data.get("heroes", [])])