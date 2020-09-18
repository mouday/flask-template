# -*- coding: utf-8 -*-

from application.views.api.commons.result import result
from application.models.user import UserModel


class User(object):
    @classmethod
    def index(cls, uid):
        user = UserModel.select_by_id(uid)
        return result(user)
