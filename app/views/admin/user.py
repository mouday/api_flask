# -*- coding: utf-8 -*-
from flask import request

from app.api_flask.api_blueprint import ApiBlueprint
from app.api_flask.api_exception import ApiException

app = ApiBlueprint('admin.user', __name__)


@app.post("/info")
def info():
    return {'name': 'Tom', 'age': 23}


@app.post("/json")
def handle_json():
    return request.json


@app.post('/error')
def error():
    raise ApiException('my error')
