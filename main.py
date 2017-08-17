from flask import Flask, Blueprint
import json
import os
import sys
sys.path.append("./views")
import api
import post
import database
import traceback
import logging
from logging import FileHandler
from logging import Formatter


app = Flask(__name__)
app.register_blueprint(api.mod)
app.register_blueprint(post.mod)

appFileHandler = FileHandler(filename=os.path.abspath('flask.log'))
appFileHandler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))

app.logger.addHandler(appFileHandler)
database.init_db()

@app.teardown_request
def shutdwon_session(exception=None):
    database.db_session.remove()


@app.errorhandler(500)
def internal_server_error(e):
    app.logger.exception('error 500: %s', e)

    return "500"




if __name__ == '__main__':

    app.run(host='127.0.0.1', port=2000)
   

