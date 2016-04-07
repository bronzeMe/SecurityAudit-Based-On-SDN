# coding=utf-8
import MySQLdb
import time



def createConnection(host, user, passwd, db):
    try:
        conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        return conn
    except Exception, e:
        print 'connect to the mysql database failed'
        print e


# the selectField parameter's type is tuple
def loadDataFromDB(tablename, selectField=("*")):
    conn = createConnection("127.0.0.1", 'developer', 'yunhe127', 'SecurityEventDataBase')
    cursor = conn.cursor()
    selecttmp = ''
    for i in range(len(selectField)):
        selecttmp += selectField[i] + ','
    selecttmp = selecttmp[:len(selecttmp) - 1]  # remove the last ','
    # print selecttmp
    sqlcmd = "select " + selecttmp + " from " + tablename
    # print sqlcmd
    result = cursor.execute(sqlcmd)
    data = cursor.fetchmany(result)  # return tuple type
    # print 'internal function result test'
    # print data
    cursor.close()
    conn.commit()
    conn.close()
    return data


def preprocessData(data):
    '''the parameter's type is tuple,'data' is tuple.
    the method's function is transform the tuple into a list'''

    retlist = []
    for item in data:
        tmplist = []
        for minitem in item:
            if minitem == "" or minitem is None:  # filter empty field
                pass
            else:
                tmplist.append(minitem)
        retlist.append(tmplist)
    return retlist

def processTimeStampField(timestampData):
    timeformat='%H:%M:%S'
    timefield=timestampData.split(' ')[1]
    t=time.strptime(timefield,timeformat)
    if t.tm_hour<12:
        return 'am'
    elif t.tm_hour<20:
        return 'pm'
    else:
        return 'night'

def preprocessTimeStampData(data):
    '''the data contain timestamp field
     transform the timestamp field into [am] or [pm].e.g 18:41:26--->pm 09:45:34-->am
     timestamp is the first field'''
    retlist = []
    for item in data:
        tmplist = []
        processTimeStampFlag=True
        for minitem in item:
            if minitem == "" or minitem is None:  # filter empty field
                pass
            else:
                if(processTimeStampFlag):
                    timeitem=processTimeStampField(minitem)
                    tmplist.append(timeitem)
                    processTimeStampFlag=False
                else:
                    tmplist.append(minitem)
        retlist.append(tmplist)
    return retlist

if __name__=='__main__':
    # result is total item count
    data = loadDataFromDB("userlog", ('timestamp','src_ip', 'dst_ip', 'src_port', 'dst_port', 'protocol', 'service'))
    print data
    for item in data:
        print type(item)
        print item

    print '=' * 100
    datalist = preprocessData(data)
    print datalist
    print '=' * 100
    for item in datalist:
        print item
    datalistTime=preprocessTimeStampData(data)
    print '-' * 100
    for item in datalistTime:
        print item