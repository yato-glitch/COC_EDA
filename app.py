import os
import streamlit as st
import pandas as pd
import plotly.express as px
from fetch_api import fetch_player_data  
from eda_coc import plot_troop_levels, plot_trophy_progression, plot_clan_contributions  
from recommendation import get_base_army_compositions

def main():
    st.set_page_config(page_title="Clash of Clans EDA", layout="wide")
    
   
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("C:/Users/bhard/Desktop/coc_edaproject/857565.jpg", width=450)
    with col2:
        st.image("C:/Users/bhard/Desktop/coc_edaproject/782659.jpg", width=450)
    
    st.markdown("""
        <h1 style='text-align: center; color: white;'>Clash of Clans Player Analysis & Strategy Recommendations</h1>
        <style>
            body {
                background-color: #0d1117;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center;'>
            <p style='font-size: 18px;'>Enter your Clash of Clans Player Tag below to fetch detailed analysis.</p>
        </div>
    """, unsafe_allow_html=True)
    
    player_tag = st.text_input("Enter your Clash of Clans Player Tag:", max_chars=15)
    if not player_tag:
        st.warning("Please enter a valid player tag.")
        return
    
    if st.button("Fetch Data"):
        with st.spinner("Fetching player data..."):
            api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImEyMDY3OWM4LTYzMDUtNGI5Mi04YjFjLTdhODM3MmExMjA3MCIsImlhdCI6MTc0MDk3NDA3Miwic3ViIjoiZGV2ZWxvcGVyL2U5MjVhMWRjLWQxMzItYTZmNC1kZjQ4LTJjMTIzZmY4NmE5NyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMy4xODkuNzEuMjIzIiwiMTUyLjU4LjEyNC44NyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.UU0zBD2o0afn3WDOuOg3K_E7WRMndmWl3IDj1kF6Akksz7W7NBmQ3dop4n5sDo4QZuN6UTyXUjxi8ipd6IX3tw"
            player_data = fetch_player_data(player_tag, api_key)
            
            if player_data:
                st.success("Player data fetched successfully!")
                
                st.subheader("Player Card")
                avatar_url = player_data.get('avatarUrl', None)
                if avatar_url:
                    st.image(avatar_url, width=150)
                else:
                    st.image("C:/Users/bhard/Desktop/coc_edaproject/avatar.jpg", width=150) 
                
                st.write(f"**Name**: {player_data.get('name', 'Unknown')}")
                st.write(f"**Tag**: {player_data.get('tag', 'Unknown')}")
                st.write(f"**Town Hall Level**: {player_data.get('townHallLevel', 'Unknown')}")
                st.write(f"**Trophies**: {player_data.get('trophies', 'Unknown')}")
                st.write(f"**War Stars**: {player_data.get('warStars', 'Unknown')}")
                st.write(f"**Best Trophies**: {player_data.get('bestTrophies', 'Unknown')}")
                
                st.subheader("Troop Levels Analysis")
                troop_fig = plot_troop_levels(player_data, filter_main_base=True)  
                st.plotly_chart(troop_fig)
                
                st.subheader("Trophy Progression")
                trophy_fig = plot_trophy_progression(player_data)
                st.plotly_chart(trophy_fig)
                
                st.subheader("Clan Contributions")
                clan_fig = plot_clan_contributions(player_data)
                st.plotly_chart(clan_fig)
                
                st.subheader("Recommended Attack Strategies")
                attack_strategies = get_base_army_compositions().get(player_data.get("townHallLevel", "Unknown"), {}).get('attack', {})
                st.json(attack_strategies)
                
                st.subheader("Recommended Farming Strategy")
                farming_strategy = get_base_army_compositions().get(player_data.get("townHallLevel", "Unknown"), {}).get('farming', {})
                st.json(farming_strategy)
            else:
                st.error("Failed to fetch player data. Please check the player tag and try again.")
    
if __name__ == "__main__":
    main()
