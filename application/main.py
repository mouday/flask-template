# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, unicode_literals

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from application.views.api.index import api_view
from application.views.index import index_view
from application import config

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

# 加载配置
app.config.from_object(config)

# 配置蓝图
app.register_blueprint(blueprint=index_view, url_prefix='/')
app.register_blueprint(blueprint=api_view, url_prefix='/api')
