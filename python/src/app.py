from flask import Flask, request
import os.path
import datetime as dt
app = Flask(__name__)


def init_temperature_file():
    if not os.path.exists('temperature.csv'):
        with open('temperature.csv', 'a') as temperature_file:
            temperature_file.write('datetime,temperature\n')


@app.route('/temperature', methods=['GET'])
def get_temperatures():
    init_temperature_file()

    with open('temperature.csv', 'r') as temperature_file:
        return temperature_file.read()


@app.route('/temperature', methods=['POST'])
def record_temperature():
    if 'temperature' not in request.json:
        return 'Expected request body to contain "temperature"', 403

    init_temperature_file()

    with open('temperature.csv', 'a') as temperature_file:
        print('%s,%s' % (dt.datetime.now(), request.json['temperature']))
        temperature_file.write('%s,%s\n' % (dt.datetime.now(), request.json['temperature']))

    return '{"message": "ok"}'
