import requests
import streamlit as st

# Function to fetch player data from the Clash of Clans API
def fetch_player_data(player_tag):
    # Fetch the API key securely from Streamlit secrets
    api_key = st.secrets["general"]["api_key"]  # Make sure to set this in secrets.toml
    
    # Format the URL for the player
    url = f'https://api.clashofclans.com/v1/players/%23{player_tag[1:]}'
    
    # Set the headers with the API key
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    
    # Send the request to the Clash of Clans API
    response = requests.get(url, headers=headers)
    
    # Check the response status and return data or None
    if response.status_code == 200:
        return response.json()
    else:
        return None






