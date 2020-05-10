#!/usr/bin/env python

from flask import Flask, request, abort
from flask_graphql import GraphQLView
from global_schema import schema
from database import db_session
import os
from flask_cors import CORS
import mail

app = Flask(__name__)

app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS')
# app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL')

# Mail sender:
@app.route('/mail/send', methods=['POST'])
def send_mail():
    parameters = request.json

    if not parameters or not 'name' or not 'sender' or not 'subject' or not 'message' in parameters:
        abort(400)

    return mail.send(app, parameters)

# GraphQL:
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
cors = CORS(app, resources={r"/graphql": {"origins": "*", "supports_credentials": True}})

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', '7000'),
            host=os.environ.get('HOST', '0.0.0.0'))
