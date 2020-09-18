# -*- coding: utf-8 -*-
from flask import render_template


class Index(object):
    @staticmethod
    def index():
        return render_template("index.html")
