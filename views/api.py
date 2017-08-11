from flask import Blueprint, request
from config import RESOURCE_PATH
import controller

mod = Blueprint('api', __name__, template_folder='templates')


@mod.route('/')
def hello_world():
    return 'Hello World!'

@mod.route('/api/comment/<id>')
def comment(id):
    ret = {}
    with open(RESOURCE_PATH + '/comment_' + id + '.json', 'r') as fp:
        str = fp.read()

    return str

@mod.route('/api/passages/latest')
def passages_latest():
    pass

@mod.route('/api/passages/hotest')
def passages_hotest():
    pass

@mod.route('/api/nodes')
def nodes():
    pass

@mod.route('/api/passages/node')
def passages_node():
    node_id = request.args('node_id', '')



@mod.route('/api/detail/passage')
def detail_passage():
    passage_id = request.args('passage_id', '')

@mod.route('/api/detail/comment')
def detail_comment():
    passage_id = request.args('passage_id', '')