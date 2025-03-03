#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
api_key="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImMyMGIyMzU3LWFlOTgtNDQ5MS04OWIyLThiY2YzNjViZGJmZSIsImlhdCI6MTc0MDkzNTMxMywic3ViIjoiZGV2ZWxvcGVyL2U5MjVhMWRjLWQxMzItYTZmNC1kZjQ4LTJjMTIzZmY4NmE5NyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMy4xODkuNzEuMjIzIl0sInR5cGUiOiJjbGllbnQifV19.1qguaT-hDNNSAntCiFzKqk4jVDMON7w8ywSDOJoLmkr7mk4Re7lgnCTsJeY3mMNgJOBTIM1TQ2mgrreZFwmZUg"
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





