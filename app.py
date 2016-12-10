#!/usr/bin/env python

from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
   return "TEST 123 Home Page"

@app.route('/demo')
def demo():
    return "DEMO PAGE"


if __name__ == '__main__':
   app.run(host="0.0.0.0",debug=True)
