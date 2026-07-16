from flask import Flask
import requests

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/")
def home():
    lat, lon = 38.95, -92.33 # Example coordinates for Columbia, Missouri
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    data = requests.get(url).json()
    weather = data["current_weather"]
    return f"<h1>Columbia, MO</h1><p>Temperature: {weather['temperature']}°C</p><p>Wind: {weather['windspeed']} km/h</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

