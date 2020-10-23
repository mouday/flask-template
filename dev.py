# -*- coding: utf-8 -*-

"""自动重载前端模板"""

from flask_script import Manager
from run import app
from livereload import Server

manager = Manager(app)


@manager.command
def dev():
    live_server = Server(app.wsgi_app)
    live_server.watch("static/*.*")
    live_server.watch("templates/*.*")
    live_server.serve(open_url_delay=True)


if __name__ == '__main__':
    # $ python dev.py
    manager.run(default_command="dev")
