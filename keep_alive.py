from flask import Flask
from threading import Thread
from os import getenv

app = Flask('')

@app.route('/')
def home():
    return "running now"


def run():
    app.run(host='0.0.0.0', port=getenv('PORT'))


def keep_alive():
    t = Thread(target=run)
    t.start()
