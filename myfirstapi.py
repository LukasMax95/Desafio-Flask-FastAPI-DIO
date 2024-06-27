import pandas as pd
from datetime import datetime
from flask_ngrok import run_with_ngrok
import flask as flk
import random as rk

app = flk.Flask(__name__)
run_with_ngrok(app)

d = {
    "author": "Lukas Maximo",
    "text": "Hello Wolrd, Mongo DB!",
    "tags": ["Mongo DB", "Python", "Pymongo", "Hello Wolrd"],
    "date": datetime.now()
}

@app.route("/")
def home():
    return f"""
<marquee><h3> My First Api! </h3></marquee>
"""

@app.route("/input")
def input():
    return flk.jsonify(d)

@app.route('/output', methods = ['GET', 'POST'])
def predJson():
    pred = rk.choice(["positive", "negative"])
    nd = d
    nd["prediction"] = pred
    print(flk.jsonify(nd))
    return """
    <style>
    h3{
        font-family: monospace;
    }"""+f"""
    </style>
    
    <marquee><h3><br>{nd}<br></h3></marquee>
    """

app.run()