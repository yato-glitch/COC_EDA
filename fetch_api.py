import streamlit as st
import requests

def fetch_player_data(player_tag):
  
    api_key ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjYzZTg1Yjk2LTc4NjgtNDg5My1hOTc1LTFkODkyODFhMDQ1ZCIsImlhdCI6MTc0MTA5NDM1Nywic3ViIjoiZGV2ZWxvcGVyL2U5MjVhMWRjLWQxMzItYTZmNC1kZjQ4LTJjMTIzZmY4NmE5NyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM1LjIwMS4xMjcuNDkiXSwidHlwZSI6ImNsaWVudCJ9XX0.VhLhGSTeq9uOL56XZmqRfi4s_ZKyNZBSaOb-0gOFm7sM5G16sv40vzenRmrkSnz2OPxEppTZbYJItpPdzJ9OJg"
    
    url = f"https://api.clashofclans.com/v1/players/%23{player_tag[1:]}"
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json() 
    else:
        return None
