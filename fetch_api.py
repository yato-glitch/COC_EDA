import streamlit as st
import requests

def fetch_player_data(player_tag):
  
    api_key ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjExNDdmMTM0LWMyOGItNDU1MC04Nzk4LTc0Nzg5ZDcxZGY2YyIsImlhdCI6MTc0MTA5MzU1NSwic3ViIjoiZGV2ZWxvcGVyL2U5MjVhMWRjLWQxMzItYTZmNC1kZjQ4LTJjMTIzZmY4NmE5NyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM1LjIzMC4xMjcuMTUwIiwiMzUuMjAzLjE1MS4xMDEiLCIzNC4xOS4xMDAuMTM0IiwiMzQuODMuMTc2LjIxNyIsIjM1LjIzMC41OC4yMTEiXSwidHlwZSI6ImNsaWVudCJ9XX0.kUaGS59rDPFai7QUUpnLuDvhYPHnaBSPx6BY1V0JGCIVuYgW-iHxkQffvh2aHBkfv5cHBoF7A2hm_E5X8ZuCFg"
    
    url = f"https://api.clashofclans.com/v1/players/%23{player_tag[1:]}"
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json() 
    else:
        return None
