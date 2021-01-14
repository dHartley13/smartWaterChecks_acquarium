import os 
import glob
import time
import json
import datetime
import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
from dataclasses import dataclass
import flask


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

device_file = '/sys/bus/w1/devices/28-3c01d607eefb/w1_slave'

X = deque(maxlen=100)
Y = deque(maxlen=100)
server = flask.Flask(__name__)
server.config["DEBUG"] = True

@dataclass(unsafe_hash=True)
class TemperatureItem:
    '''Class for keeping track of an item in inventory.'''
    degrees_celcius: float
    degrees_fahrenheit: float
    ts: int

def read_temp_raw():
    with open(device_file, 'r') as file:
        lines = list(file.readlines())
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        #print("in the if")
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        ts = int(datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S'))
        
        #Changed output to return dict so i get a response when i curl localhost
        _temp = {
            "Celsius": temp_c,
            "Farenheit":temp_f,
            "ts":ts
            }
        return _temp

@server.route('/', methods=['GET', 'POST'])
def home():
    return read_temp()


if __name__ == '__main__':
    server.run()    
 