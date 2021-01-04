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


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = '/sys/bus/w1/devices/28-3c01d607eefb/w1_slave'

X = deque(maxlen=100)
Y = deque(maxlen=100)
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=60000,
            n_intervals=0
        ),
    ]
)

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
        _temp = TemperatureItem(temp_c,temp_f,ts)
        #_temp = json.dumps({'degreesCelcius':temp_c, 'degreesFarenheit': temp_f, 'ts':ts})
        return _temp
    # return TemperatureItem(random.uniform(0,1),random.uniform(0,1),int(datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')))

@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph_scatter(n):
    temp: TemperatureItem = read_temp()
    X.append(temp.ts)
    Y.append(temp.degrees_celcius)
    print(Y)
    print(X)

    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )

    return {'data': [data],
            'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]), yaxis=dict(range=[min(Y), max(Y)]), )}

#while True:
#    print(read_temp().ts)

if __name__ == '__main__':
    app.run_server()
