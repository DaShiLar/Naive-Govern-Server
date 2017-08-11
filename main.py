from flask import Flask, Blueprint
import json
import os
import sys
sys.path.append("./views")
import api
import database

app = Flask(__name__)
app.register_blueprint(api.mod)

database.init_db()

@app.teardown_request
def shutdwon_session(exception=None):
    database.db_session.remove()



if __name__ == '__main__':
    app.run()

   

