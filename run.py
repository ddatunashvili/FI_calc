#!/usr/bin/python
# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*
from flask import Flask,redirect, url_for, render_template, request, session, flash
import pprint
import requests
from functions import *
app = Flask(__name__)

# ტოკენი
app.secret_key = "app" 

'''
# debit credits  data structure
data ={ 
    "debits":{
        "salary":100,
        "savings":40
    },
    "credits":{
        "transport":30,
        "bills":10
    }
}
acces all data by variable = get_data("person name and surname") myexample is without name : get_data("david")

# you can acces from index.html or run.py or importing module in any file

database = get_data("david")
name = database["name"]
total = database["total"]
change = database["change"]
debits = database["debits"]
credits = database["credits"]

'''


db = get_data("david")
balance = sum(db["debits"].values())-sum(db["credits"].values())
name = db['name']

# root directory decorator
@app.route("/", methods=["POST","GET"])
def choose_topic():
    if request.method == "POST":
        topic = request.form["topic"]
        session["topic"] = topic
        return redirect(url_for("choose"))
    else:
        
        return render_template("index.html", balance  =  balance, data = db,name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True) 