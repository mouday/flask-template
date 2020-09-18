# -*- coding: utf-8 -*-

from flask import Flask

from views.api import api_view
from views.index.index import index_view

app = Flask(__name__)

# 加载配置
app.config.from_object('config')

# 配置蓝图
app.register_blueprint(blueprint=index_view, url_prefix='/')
app.register_blueprint(blueprint=api_view, url_prefix='/api')