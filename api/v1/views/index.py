#!/usr/bin/python3
""" Initialize the views """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    return jsonify({'status': 'ok'})