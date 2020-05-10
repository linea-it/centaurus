from flask_mail import Mail, Message
from flask import render_template, jsonify
import os

def send(app, parameters):
  mail = Mail(app)

  success_template = render_template(
    'home.html',
    name=parameters['name'],
    email=parameters['sender'],
    message=parameters['message'],
  )

  msg = Message(
    html=success_template,
    sender=parameters['sender'],
    subject=parameters['subject'],
    recipients=[os.environ.get('MAIL_USERNAME')]
  )
  mail.send(msg)
  return jsonify({
    'success': True,
  })
