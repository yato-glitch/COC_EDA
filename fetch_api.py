import streamlit as st
import requests

def fetch_player_data(player_tag):
    # Retrieve the API key directly from st.secrets
    api_key = st.secrets["general"]["api_key"]
    
    url = f"https://api.clashofclans.com/v1/players/%23{player_tag[1:]}"
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the player data as JSON
    else:
        return None
