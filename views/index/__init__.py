# -*- coding: utf-8 -*-

from views.index.controller.index import Index
from views.index.index import index_view

index_view.add_url_rule("/", view_func=Index.index)
