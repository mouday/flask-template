# -*- coding: utf-8 -*-
from flask import jsonify


class Result(object):

    @classmethod
    def result(cls, data, msg, code):
        """统一返回的格式"""

        return jsonify({
            'data': data,
            'msg': msg,
            'code': code
        })

    @classmethod
    def success(cls, data, msg='success', code=0):
        return cls.result(data, msg, code)

    @classmethod
    def error(cls, data, msg='error', code=-1):
        return cls.result(data, msg, code)
