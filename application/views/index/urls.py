# -*- coding: utf-8 -*-

from application.views.index.controller.index import Index
from application.views.index.main import index_view

index_view.add_url_rule("/", view_func=Index.index)
