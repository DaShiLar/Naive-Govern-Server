from flask import Flask
import json
import os
import sys

RESOURCE_PATH = os.path.dirname(os.path.abspath(__file__))+'/static/'

HOTEST_STANDARD = 3

LATEST_STANDARD = 10

PASSAGE_PER_NODE = 20

DB_CONNECT_STRING = 'mysql+pymysql://root:She68105028@localhost:3306/govern?charset=utf8'