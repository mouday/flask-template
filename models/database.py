# -*- coding: utf-8 -*-

from myquery import DataBase, Table

from config import MYSQL_URL


class CustomDataBase(DataBase):
    def _before_execute(self, operation, params):
        """使数据库保持链接"""
        if not self.is_connected():
            self.reconnect()
        return super()._before_execute(operation, params)


db = CustomDataBase(db_url=MYSQL_URL)


class BaseModel(Table):
    """基类，用于被继承"""

    database = db
