#!/usr/bin/env python

from flask import Flask, render_template
from flask_graphql import GraphQLView
from global_schema import schema
from database import db_session
import os
from flask_cors import CORS


app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
cors = CORS(app, resources={r"/graphql": {"origins": "*", "supports_credentials": True}})

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', '7000'),
            host=os.environ.get('HOST', '0.0.0.0'))
