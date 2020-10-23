# -*- coding: utf-8 -*-

from myquery import ReconnectionDataBase, Model

from application.config import MYSQL_URL


db = ReconnectionDataBase(db_url=MYSQL_URL)


class BaseModel(Model):
    """基类，用于被继承"""

    database = db
