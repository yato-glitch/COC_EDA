import streamlit as st
import requests

def fetch_player_data(player_tag):
    # Retrieve the API key directly from st.secrets
    api_key ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjA2NGM5YjkyLTU0OTctNGE4YS1iMjVlLWI5ZjQ2OTFhMzk3YyIsImlhdCI6MTc0MTAyNDA3MCwic3ViIjoiZGV2ZWxvcGVyL2U5MjVhMWRjLWQxMzItYTZmNC1kZjQ4LTJjMTIzZmY4NmE5NyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMy4xODkuNzEuMjIzIl0sInR5cGUiOiJjbGllbnQifV19.wrPYQYBEnAbPrP_rWPjroU0oxAtYNgKYA_yOElLF8I4QgAxrIUShAQfwvqJMe1fkQb2oE3hrA4l5YKMuQ2gHNA"
    
    url = f"https://api.clashofclans.com/v1/players/%23{player_tag[1:]}"
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the player data as JSON
    else:
        return None
