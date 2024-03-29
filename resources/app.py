import os

import pandas as pd
import numpy as np
import requests
import json

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

my_data = []


@app.route("/data")
def symbol():
    
    stock = my_data[0]["symbol"]

    # print(stock)

    todays_day = date.today() 
    start = datetime.datetime(2019, 1, 1)
    end = todays_day

    df = web.DataReader(stock, 'yahoo', start, end)
    df.reset_index(inplace=True)
    df = df.drop(columns=["Open","High","Low","Adj Close","Volume"])

    data = {
        "Date":df.Date.tolist(),
        "Close": df.Close.values.tolist()
    }

    return jsonify(data)


@app.route('/send', methods=['GET','POST'])
def my_form_post():
    if request.method == 'POST':

        stock = request.form['symbol']
        print(stock)
 
        data = {
            "symbol":text
        }
        my_data.append(data)

        return "Thank You"
    return render_template("index.html")



if __name__ == "__main__":
    app.run()
