from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import json


app = Flask(__name__, static_url_path='', static_folder='build', template_folder='build')
CORS(app)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/api", methods=['POST'])
def get_weather():
    request_body = request.json
    city = request_body['city']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=aa61907de23846f2a309d33d56948612"
    response = requests.get(url)
    response = json.loads(response.text)

    if response['cod'] == 200:
        weather = response['weather'][0]['main']
        return weather
    else:
        return "err"
