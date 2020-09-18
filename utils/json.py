# -*- coding: utf-8 -*-
from datetime import datetime, date

from flask.json import JSONEncoder as _JSONEncoder

from config import DATETIME_FORMAT, DATE_FORMAT


class JSONEncoder(_JSONEncoder):
    """格式化json中的时间字段"""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime(DATETIME_FORMAT)
        elif isinstance(obj, date):
            return obj.strftime(DATE_FORMAT)
        else:
            return JSONEncoder.default(self, obj)
