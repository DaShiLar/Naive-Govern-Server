from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Time, Text
from database import Base
import time
from utils import generateTime

UP = 0
MUTUAL = 1
DOWN = 2



class Passage(Base):

    __tablename__ = 'passage'

    passage_id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(Text)
    passage_owner = Column(String(30))
    public_time = Column(Time)
    passage_type = Column(String(30))
    passage_content = Column(Text)
    up = Column(Integer)
    mutual = Column(Integer)
    down = Column(Integer)
    commentNumber = Column(Integer)

    def __init__(self, title, passage_type, passage_content):
        self.title = title
        self.public_time = generateTime()
        self.passage_type = passage_type
        self.passage_content = passage_content
        self.up = 0
        self.mutual = 0
        self.down = 0
        self.commentNumber = 0






class Comment(Base):

    __tablename__ = 'comment'

    comment_id = Column(Integer, autoincrement=True, primary_key=True)
    passage_id = Column(ForeignKey('passage.passage_id'))
    user_name = Column(String(30))
    comment_time = Column(Time)
    comment_incline = Column(Integer)
    comment_content = Column(Text)

    def __init__(self, passage_id, comment_incline, comment_content):
        ##TODO 之后user_name可能会恢复正常，目前全是root
        self.user_name = "root"
        self.passage_id = passage_id
        self.comment_time = generateTime()
        self.comment_incline = comment_incline
        self.comment_content = comment_content