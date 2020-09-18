# -*- coding: utf-8 -*-

from views.api.controller.user import User
from views.api.index import api_view

api_view.add_url_rule('/user/<int:uid>', view_func=User.index)
