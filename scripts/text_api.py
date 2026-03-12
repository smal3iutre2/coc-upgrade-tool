# -*- coding: utf-8 -*-
"""
@Time    : 2026/3/12 1:26
@Author  : Minghe Liu
@File    : text_api.py
@Description : 
"""
import urllib.parse

import requests

TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImUzNTVjNmRhLTA3MTctNGQzZi1hZGVmLWNkYTE5ZDIyZGU3ZiIsImlhdCI6MTc3MzI5NjQyNywic3ViIjoiZGV2ZWxvcGVyL2M4M2ZjODZiLTc1N2Et ZWQ0Mi1iNTc0LTU3NjMwNDhlOWI4MiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM1LjE0NC42OC4xMzkiXSwidHlwZSI6ImNsaWVudCJ9XX0.4Yyt4iwnleZfG7_UCbUL_7j1YwJ-MSkgPpSwijt1xywheYtqqlllUXyBxc3FTaPsjxYQBkxGh1RDbCp_G9Iglg'
player_tag = '#GV8PJLQQ8'
api_url = f'https://api.clashofclans.com/v1/players/{urllib.parse.quote(player_tag)}'

headers = {
    'Authorization': f'Bearer {TOKEN}'
}


def test() -> dict:
    resp: requests.Response = requests.get(url=api_url, headers=headers)
    assert resp is not None and resp.status_code == 200, f'request failed'
    return resp.json()


if __name__ == '__main__':
    print(api_url)
    res = test()
    for k, v in res.items():
        print(k, v)
