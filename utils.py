import time
import traceback


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
