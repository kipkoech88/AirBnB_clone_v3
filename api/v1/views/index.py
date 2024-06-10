#!/usr/bin/python3
""" Initialize the views """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """ retuen the status of the api"""
    data = {
    "status": "ok"
    }
    res = jsonify(data)
    res.status_code = 200
    return res
