# -*- coding: utf-8 -*-

"""
配置文件
"""

from environs import Env

from application.config.default import *


# 获取环境数值 .env
env = Env()
env.read_env()
FLASK_ENV = env.str('FLASK_ENV')


# 数据库链接配置，安全起见，写在.env配置文件中，不上传git
MYSQL_URL = env.str('MYSQL_URL')


# 判断是否为生产环境
if FLASK_ENV == "production":
    from application.config.production import *
else:
    from application.config.development import *
