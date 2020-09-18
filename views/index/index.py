# -*- coding: utf-8 -*-

"""
页面
"""

from flask import Blueprint, render_template

index_view = Blueprint(name="index", import_name=__name__)


@index_view.app_errorhandler(404)
def handle_404_error(err):
    """自定义全局404页面"""
    return render_template("404.html")
