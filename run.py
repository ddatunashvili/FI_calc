#!/usr/bin/python
# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*
from flask import Flask,redirect, url_for, render_template, request, session, flash


app = Flask(__name__)


# ტოკენი
app.secret_key = "app" 





# root directory decorator
@app.route("/")
def index():
    return render_template('index.html')






if __name__ == "__main__":
    app.run()