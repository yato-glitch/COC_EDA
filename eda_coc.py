import pandas as pd
import plotly.express as px

def plot_troop_levels(player_data, filter_main_base=True):
    troops = player_data.get("troops", [])
    troop_data = []
    
    for troop in troops:
        name = troop["name"]
        level = troop["level"]
        is_builder_base = troop.get("village", "home") == "builderBase"
        
        if filter_main_base and is_builder_base:
            continue  
        
        troop_data.append({"Troop": name, "Level": level})
    
    df = pd.DataFrame(troop_data)
    
    print(df) 
    print("Is DataFrame empty?", df.empty)  
    
    if df.empty:
        return px.bar(title="No Troop Data Available", x=[], y=[])
    
    fig = px.bar(df, x="Troop", y="Level", title="Troop Levels", labels={"Level": "Troop Level"})
    fig.update_layout(xaxis_tickangle=-90, xaxis_tickfont_size=12)  
    return fig

def plot_trophy_progression(player_data):
    trophies = player_data.get("trophies", 0)
    best_trophies = player_data.get("bestTrophies", 0)
    
    df = pd.DataFrame({
        "Category": ["Current", "Best"],
        "Trophies": [trophies, best_trophies]
    })
    
    fig = px.line(df, x="Category", y="Trophies", title="Trophy Progression", markers=True, labels={"Trophies": "Trophy Count"})
    fig.update_traces(text=df["Trophies"], textposition="top center")
    fig.update_layout(yaxis=dict(title="Trophy Count"))
    return fig

def plot_clan_contributions(player_data):
    donations = player_data.get("donations", 0)
    received = player_data.get("donationsReceived", 0)
    
    df = pd.DataFrame({
        "Type": ["Donated", "Received"],
        "Count": [donations, received]
    })
    
    fig = px.pie(df, names="Type", values="Count", title="Clan Contributions")
    return fig
