#!/usr/bin/python
# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*
from os import execv
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
data ={ 
    "debits":{
        "salary":1,
        "savings":1,
        "gift":1,
        "lend":1
    },
    "credits":{
        "transport":1,
        "bills":1,
        "fun":1,
        "food":1
    }
}
# modify_data("Datunashvili", mode="add",total=100,data=data)
# root directory decorator
@app.route("/", methods=["POST","GET"])
def main():

    db = get_data("Datunashvili")
    balance = sum(db["debits"].values())-sum(db["credits"].values())
    name = db['name']
    totaldb = sum(db["debits"].values())
    totalcr = sum(db["credits"].values())
    totalb = db["total"]
    if request.method == "POST":
        try:
            debit = request.form["dname"]
            dvalue = request.form["dvalue"]
            db["debits"][debit] = int(dvalue)
            modify_data(name, mode="change" ,total=totalb,data=db)
            return redirect(url_for("main"))
        except:
            try:
                credit = request.form["cname"]
                cvalue = request.form["cvalue"]
                db["credits"][credit] = int(cvalue)
                modify_data(name,mode="change" ,total=totalb,data=db)
                return redirect(url_for("main"))
            except:
                totalb = request.form["totalb"]
                modify_data(name,mode="change" ,total=int(totalb),data=db)
                return redirect(url_for("main"))

        return render_template("index.html", totaldb= totaldb ,total=totalb, totalcr=totalcr,balance  =  balance, data = db,name=name)
   
        # return redirect(url_for("main"))
    else:      
        return render_template("index.html", totaldb= totaldb ,total=totalb, totalcr=totalcr,balance  =  balance, data = db,name=name)


if __name__ == "__main__":
    app.run( port=80,debug=True) 