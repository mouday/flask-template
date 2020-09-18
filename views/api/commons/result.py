# -*- coding: utf-8 -*-
from flask import jsonify


def result(data, msg='ok', code=0):
    """统一返回的格式"""
    return jsonify({
        'data': data,
        'msg': msg,
        'code': code
    })
