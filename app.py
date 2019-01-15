#app.py
from flask import Flask, request, render_template
import urllib
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.dates import date2num

from io import BytesIO

import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plot/btc")
def plot_btc():

    # Obtain query parameters
    start = datetime.strptime(request.args.get("start", default="2017-12-01", type=str), "%Y-%m-%d")
    end = datetime.strptime(request.args.get("end", default="2018-12-01", type=str), "%Y-%m-%d")
    aval = request.args.get("aval", default=15, type=float)
    place=request.args.get("place", default="Nagoya",type=str)
    place2=request.args.get("place2", default="Naha",type=str)
    place3=request.args.get("place3", default="Sapporo",type=str)
    
    df = pd.read_csv("temperature.csv", index_col = 0, parse_dates=True)
    
    
    fig = plt.figure(figsize=(10,5),dpi=100)

    ax= fig.add_subplot(211)
    ax2= fig.add_subplot(212)
    
    
    
    ax.plot(df[ place] ,label=place)
    ax.plot(df[ place2] ,label=place2)
    ax.plot(df[ place3] ,label=place3)
    if start > end:
        start, end = end, start
    if (start + timedelta(days=7)) > end:
        end = start + timedelta(days=7)

    png_out = BytesIO()

    ax.set_xlim([start, end])
    plt.ylim(ymax=32)
    plt.ylim(ymin=-8)
    
    
    ax.set_ylabel("temperature")
    plt.xticks(rotation=30)
    
    
    
    df['average'] = (df[place] + df[place2]+ df[place3])/3
    df["Place1"] = df[place]-df['average']
    df["Place2"] = df[place2]-df['average']
    df["Place3"] = df[place3]-df['average']
    ax2.plot(df[ "Place1"] ,label=place)
    ax2.plot(df[ "Place2"] ,label=place2)
    ax2.plot(df[ "Place3"] ,label=place3)
    ax2.set_ylim([-aval, aval])
    ax2.set_ylabel("Temperature difference from average")
    ax2.set_xlim([start, end])
    plt.legend(loc='upper right')
    


    plt.savefig(png_out, format="png", bbox_inches="tight")
    img_data = urllib.parse.quote(png_out.getvalue())
    
    


    return "data:image/png:base64," + img_data





if __name__ == "__main__":
    app.run(debug=True, port=5000)
