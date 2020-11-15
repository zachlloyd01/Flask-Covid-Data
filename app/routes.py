from app import app
from flask import render_template, request
import requests, json

@app.route('/')
def index():
    raw_data = requests.get('https://covid-api.mmediagroup.fr/v1/cases')
    json_data = json.loads(raw_data.text)
    return render_template('index.html', data=json_data, title='Home')


@app.route('/nations/<nation>')
def nations(nation):
    raw_data = requests.get(f'https://covid-api.mmediagroup.fr/v1/cases?country={nation}')
    json_data = json.loads(raw_data.text)
    return render_template('nation.html', data=json_data, nation=nation, title=f'{nation} - Data')