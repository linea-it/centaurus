#!/usr/bin/env python

from flask import Flask, render_template
from database import init_db
from models import Test
from flask_graphql import GraphQLView
from schema import schema
import os

app = Flask(__name__)
app.debug = True

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.route('/')
def index():
    return render_template('test.html',
        tests=Test.query.all()
    )

if __name__ == '__main__':
    init_db()
    app.run(port=os.environ.get('PORT', '7000'),
            host=os.environ.get('HOST', '0.0.0.0'))
