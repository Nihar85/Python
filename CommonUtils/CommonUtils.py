import re
import datetime

def extractpattern_data(sourcestring,pattern):
    return re.findall(pattern,sourcestring)

def getSystemDateTime():
    print(datetime.datetime.today())
    return datetime.datetime.today()

