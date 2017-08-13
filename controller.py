from database import db_session
from models import Node, Passage, Comment
import time
import os
from sqlalchemy import or_, and_
from config import HOTEST_STANDARD , LATEST_STANDARD
import traceback


def fetchAllNodes():
    query = db_session.query(Node)
    allNodes = query.filter().all()
    print("allNode==") ##DELETE
    print (type(allNodes[0])) ##DELETE
    return allNodes


def insertNode():
    db_session.add(node)
    db_session.commit()


def fetchLatestPassages():
    ## TODO现在这里设计成去除所有内容，之后再做进一步优化
    query = db_session.query(Passage, Node)
    latestPassages = query.filter(Passage.node_id==Node.node_id).order_by(Passage.public_time.desc()).limit(LATEST_STANDARD).all()

    return latestPassages

def fetchHotestPassages():
    query = db_session.query(Passage,Node)
    hotestPassages = query.filter(Passage.node_id).filter(Passage.commentNumber>HOTEST_STANDARD).all()
    return hotestPassages


def fetchDetailPassage(passage_id):
    query = db_session.query(Passage, Node)
    detailPassage = query.filter(Passage.passage_id==passage_id).filter(Passage.node_id==Node.node_id).all()
    return detailPassage


def fetchDetailComments(passage_id):
    query = db_session.query(Comment)
    detailComments = query.filter(Comment.passage_id == passage_id).all()
    return detailComments


def fetchNodePassages(node_id):
    query = db_session.query(Passage, Node)
    nodePassageList = query.filter(Passage.node_id==node_id).filter(Passage.node_id==Node.node_id).all()
    return nodePassageList


def addComment(passage_id,comment_incline, comment_content):
    comment = Comment(passage_id, comment_incline, comment_content)
    db_session.add(comment)
    db_session.commit()

