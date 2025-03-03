#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
api_key="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImEyMDY3OWM4LTYzMDUtNGI5Mi04YjFjLTdhODM3MmExMjA3MCIsImlhdCI6MTc0MDk3NDA3Miwic3ViIjoiZGV2ZWxvcGVyL2U5MjVhMWRjLWQxMzItYTZmNC1kZjQ4LTJjMTIzZmY4NmE5NyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMy4xODkuNzEuMjIzIiwiMTUyLjU4LjEyNC44NyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.UU0zBD2o0afn3WDOuOg3K_E7WRMndmWl3IDj1kF6Akksz7W7NBmQ3dop4n5sDo4QZuN6UTyXUjxi8ipd6IX3tw"
def fetch_player_data(player_tag, api_key):
    url = f'https://api.clashofclans.com/v1/players/%23{player_tag[1:]}'
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None





