# -*- coding: utf-8 -*-

"""
接口
"""

from flask import Blueprint
from flask_cors import CORS

from application.utils.json import JSONEncoder
from application.views.api.commons.result import result

api_view = Blueprint(name="api", import_name=__name__)

# json格式化日期时间
api_view.json_encoder = JSONEncoder

# 处理跨域
CORS(api_view, supports_credentials=True)


@api_view.errorhandler(Exception)
def error_handler(e):
    """
    蓝图异常捕获
    """
    return result(data=None, msg=str(e), code=-1)


@api_view.errorhandler(500)
def error_500_handler(e):
    """
    蓝图异常捕获
    """
    return result(data=None, msg=str(e), code=-1)
