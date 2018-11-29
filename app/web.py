#!/usr/bin/env python

import os
import json
from flask import Flask, render_template
app = Flask(__name__)
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader("templates"))

import footballguys as fbgs

def get_pages():
    with open("pages.json") as pages:
        return json.loads(pages.read())

@app.route("/")
def index():
    pages = get_pages()
    return render_template("index.html", pages=pages)

@app.route("/page/<int:num>")
def page(num):
    num -= 1
    page = get_pages()[num]
    url = page["url"]
    class_ = page["class"]
    table = fbgs.retrieve_table(url, class_)
    return render_template("page.html", table=table)

@app.route("/debug")
def debug():
    return str(os.environ)

if __name__ == "__main__":
    app.run(debug=True)
