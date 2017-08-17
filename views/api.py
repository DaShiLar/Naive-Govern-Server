from flask import Blueprint, request
from config import RESOURCE_PATH
import controller
import json
import datetime
from functools import reduce
from utils import jsonDumper
import traceback

mod = Blueprint('api', __name__, template_folder='templates')


@mod.route('/')
def hello_world():
    return 'Hello World!'

@mod.route('/api/passages/latest')
def passages_latest():
    latestList = controller.fetchLatestPassages()
    print ('latestList Type')
    print (type(latestList))  #DELETE
    return jsonDumper(latestList)


@mod.route('/api/passages/hotest')
def passages_hotest():
    hotestList = controller.fetchHotestPassages()
    return jsonDumper(hotestList)


@mod.route('/api/nodes')
def nodes():
    allNodes = controller.fetchAllNodes()
    return jsonDumper(allNodes)


@mod.route('/api/passages/node')
def passages_node():
    node_id = request.args.get('node_id')
    print("nodePassageList==") ##DELETE
    nodePassageList = controller.fetchNodePassages(node_id)
    print (nodePassageList) ##DELETE

    return jsonDumper(nodePassageList)


@mod.route('/api/detail/passage')
def detail_passage():
    passage_id = request.args.get('passage_id')
    print("passage_id {0}".format(passage_id))
    detailPassage = controller.fetchDetailPassage(passage_id)
    print("detailPassage==") #DELETE
    print(detailPassage)  #DELETE
    return jsonDumper(detailPassage)


@mod.route('/api/detail/comment')
def detail_comment():

    passage_id = request.args.get('passage_id')
    print("passage_id {0}".format(passage_id))
    detail_comments = controller.fetchDetailComments(passage_id)

    return jsonDumper(detail_comments)