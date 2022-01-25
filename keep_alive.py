import random
from flask import Flask
from threading import Thread
from flask import render_template, request, jsonify
import html_styles as style
from time import sleep
import json

styles = random.choice(style.styles)


def change_style():
    while True:
        styles = random.choice(style.styles)
        return styles


app = Flask('')


@app.route('/')
def home():
    return change_style()


@app.route('/ipapi')
def ipapi():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:
        return request.environ['HTTP_X_FORWARDED_FOR']


   
@app.route('/main.py')
def mainraw():
  with open('main.py','r') as f:
    rawdata = f.read()
    return rawdata

@app.route('/testing')
def testing():
  with open('testing.py','r') as f:
    return f.read()

def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
