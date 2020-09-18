# -*- coding: utf-8 -*-

"""
配置文件
"""
import os

from application.config.default import *

# 获取环境数值
FLASK_ENV = os.getenv("FLASK_ENV")

# 数据库链接配置，安全起见，写在.env配置文件中，不上传git
MYSQL_URL = os.getenv("MYSQL_URL")

# 判断是否为生产环境
if FLASK_ENV == "production":
    from application.config.production import *
else:
    from application.config.development import *
