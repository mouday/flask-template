# -*- coding: utf-8 -*-
from flask import jsonify


def result(data=None, msg='ok', code=0):
    """统一返回的格式"""
    if data is None:
        data = dict()

    return jsonify({
        'data': data,
        'msg': msg,
        'code': code
    })
