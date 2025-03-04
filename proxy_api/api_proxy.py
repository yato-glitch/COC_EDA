from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the Clash of Clans API URL
COC_API_URL = "https://api.clashofclans.com/v1/players/{player_tag}"

# Your Clash of Clans API Key (Make sure to keep it secure)
API_KEY = "YOUR_CLASH_OF_CLANS_API_KEY"

# Define a route for the proxy to forward requests
@app.route('/api/v1/players/<player_tag>', methods=['GET'])
def get_player_data(player_tag):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    # Forward the request to the Clash of Clans API
    response = requests.get(COC_API_URL.format(player_tag=player_tag), headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)  # Set to run on your server's IP
