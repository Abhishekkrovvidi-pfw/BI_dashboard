from flask import Flask, jsonify
import requests
import pandas as pd
import sqlite3

app = Flask(__name__)

DATABASE = 'weather_data.db'

def create_connection():
    conn = sqlite3.connect(DATABASE)
    return conn

def fetch_weather_data():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': 'London',
        'appid': 'your_api_key'
    }
    response = requests.get(url, params=params)
    return response.json()

def process_weather_data(data):
    df = pd.DataFrame([data])
    df['temp'] = df['main'].apply(lambda x: x['temp'])
    df['humidity'] = df['main'].apply(lambda x: x['humidity'])
    df['weather'] = df['weather'].apply(lambda x: x[0]['description'])
    return df[['name', 'temp', 'humidity', 'weather']]

def save_to_db(df):
    conn = create_connection()
    df.to_sql('weather', conn, if_exists='replace', index=False)
    conn.close()

@app.route('/api/weather', methods=['GET'])
def get_weather():
    conn = create_connection()
    df = pd.read_sql('SELECT * FROM weather', conn)
    conn.close()
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    weather_data = fetch_weather_data()
    processed_data = process_weather_data(weather_data)
    save_to_db(processed_data)
    app.run(debug=True)