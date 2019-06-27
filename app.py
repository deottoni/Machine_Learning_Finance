import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, request
# from flask_sqlalchemy import SQLAlchemy

import datetime
from datetime import date
import pandas_datareader.data as web
from pandas import Series, DataFrame

app = Flask(__name__)



@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/data")
def data():
    todays_day = date.today() 

    start = datetime.datetime(2009, 1, 1)
    end = todays_day
    df = web.DataReader(f"{stock}", 'yahoo', start, end)
    df = df.drop(columns=["Open","High","Low","Adj Close","Volume"])
    return jsonify()

@app.route("/send", methods=["GET","POST"])
def stock():
    todays_day = date.today() 
    start = datetime.datetime(2009, 1, 1)
    end = todays_day

    if request.method == "POST":
        stock = request.form["ticker"]
        print(stock)

        df = web.DataReader(f"{stock}", 'yahoo', start, end)
        df = df.drop(columns=["Open","High","Low","Adj Close","Volume"])

    return jsonify(df)



if __name__ == "__main__":
    app.run()
