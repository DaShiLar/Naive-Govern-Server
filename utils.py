import time
import traceback
import json
import datetime
from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            print ("is instance DeclarativeMeta")
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)     # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:    # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    else:
                        fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


def jsonDumper(obj):
    ##未找到数据， 需要重新考虑
    if obj == []:
        return "None"

    str = json.dumps(obj, cls=AlchemyEncoder)
    newobjs = json.loads(str)


    try:
        ##如果newobj是tuple,说明返回值包含了多个表，则需要把两个表合并起来,重新构建返回值
        if isinstance(newobjs[0], list) or isinstance(newobjs[0], tuple):
            ret = []
            for newobj in newobjs:
                newtable = {}

                for table in newobj:
                    for key, value in table.items():
                        newtable[key] = value

                ret.append(newtable)

            return json.dumps(ret)

        ## newobj是对象，说明返回值是只包含单个表，直接返回就可以啦

        else:
            return json.dumps(newobjs)
    except:
        return 0


def generateTime():
    timeArray = time.localtime(time.time())
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


def errorlog(func):
    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except:
            with open('example.log', 'w+') as fp:
                fp.write(convertTime(time.time()))
                traceback.print_exc(file=fp)

    return wrapper
