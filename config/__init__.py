# -*- coding: utf-8 -*-

"""
配置文件
"""

import os
from config.default import *

# 获取环境数值
FLASK_ENV = os.getenv("FLASK_ENV")

# 判断是否为生产环境
if FLASK_ENV == "production":
    from config.production import *
else:
    from config.development import *
