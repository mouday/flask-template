# -*- coding: utf-8 -*-

from views.api.commons.result import result
from models.user import UserModel


class User(object):
    @staticmethod
    def index(uid):
        user = UserModel.select_by_id(uid)
        return result(user)
