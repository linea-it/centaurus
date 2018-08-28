#!/usr/bin/env python

from flask import Flask, render_template
from database import init_db
from models import Test

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('test.html',
        tests=Test.query.all()
    )

if __name__ == '__main__':
    init_db()
    app.run()
