import random

ip_address = ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4', '10.0.0.5',
              '10.0.0.6', '10.0.0.7', '10.0.0.8', '10.0.0.9', '10.0.0.10']

tcpUsualService=['http','telnet','icmp','smtp','https','ssh','ftp']
tcpPortService = {'80': 'http',
                  '23': 'telnet',
                  '22': 'ssh',
                  '21': 'ftp',
                  '20': 'ftp-data',
                  '443': 'https',
                  '25': 'SMTP',
                  '110': 'POP3',
                  '143': 'IMAP',
                  '3389': 'terminal service',
                  '1723': 'PPTP'}
tcpPort = ['80', '23', '22', '443', '20', '21', '25', '110', '3389', '1723', '143']
udpPortService = {'67': 'DHCP-server',
                  '68': 'DHCP-client',
                  '53': 'DNS',
                  '161': 'snmp',
                  '162': 'snmptrap',
                  '69': 'TFTP',
                  '123': 'ntp'
                  }
udpPort = ['69', '67', '68', '53', '161', '162', '123']
protocol = ['1', '6', '17']
protocolDescription = {'1': 'ICMP', '6': "TCP", '17': "UDP"}

def dataGenSrcIpDstIp(count):
    f=open('testDataSrcDstIP.txt','w')
    for i in range(count):
        src_ip = random.choice(ip_address)
        dst_ip = random.choice(ip_address)
        while (src_ip == dst_ip):
            dst_ip = random.choice(ip_address)
        # # ip_protocol = random.choice(protocol)
        # service=random.choice(tcpUsualService)
        src_dst=src_dst = src_ip + " " + dst_ip
        print src_dst
        f.write(src_dst+'\n')
        # f.write(dst_src+'\n')
    f.close()

def dataGenTcpServcie(count):
    f=open('testDataTcp.txt','w')
    for i in range(count):
        src_ip = random.choice(ip_address)
        dst_ip = random.choice(ip_address)
        while (src_ip == dst_ip):
            dst_ip = random.choice(ip_address)
        # ip_protocol = random.choice(protocol)
        service=random.choice(tcpUsualService)
        src_dst=src_dst = src_ip + " " + dst_ip + " " +service
        print src_dst
        f.write(src_dst+'\n')
        # f.write(dst_src+'\n')
    f.close()

def dataGenGivenField(count):
    f=open('testDataField.txt','w')
    for i in range(count):
        src_ip = random.choice(ip_address)
        dst_ip = random.choice(ip_address)
        while (src_ip == dst_ip):
            dst_ip = random.choice(ip_address)
        ip_protocol = random.choice(protocol)
        if ip_protocol == '1':
            service='ICMP'
        elif ip_protocol == '6':
            src_port = random.choice(tcpPort)
            service=tcpPortService[src_port]
        elif ip_protocol == '17':
            src_port = random.choice(udpPort)
            service=udpPortService[src_port]
        src_dst=src_dst = src_ip + " " + dst_ip + " " + ip_protocol+" "+service
        print src_dst
        f.write(src_dst+'\n')
        # f.write(dst_src+'\n')
    f.close()


def dataGenGivenSrcip(src_ip,count):
    f=open('testDataSrcipII.txt','a')
    for i in range(count):
        dst_ip = random.choice(ip_address)
        while (src_ip == dst_ip):
            dst_ip = random.choice(ip_address)
        ip_protocol = random.choice(protocol)
        src_dst = src_ip + " " + dst_ip + " " + ip_protocol
        # if ip_protocol == '1':
        #     # src_port = ""
        #     # dst_port = ""
        # elif ip_protocol == '6':
        #     # src_port = random.choice(tcpPort)
        #     # dst_port = random.randrange(4000, 65500)
        # elif ip_protocol == '17':
        #     # src_port = random.choice(udpPort)
        #     # dst_port = random.randrange(4000, 65500)
        # if src_port=="":
        #     src_dst = src_ip + " " + dst_ip + " " + ip_protocol
        #     # dst_src = dst_ip + " " + src_ip + " " + ip_protocol
        # else:
        #     src_dst = src_ip + " " + dst_ip + " " + ip_protocol + " " + str(src_port) + " " + str(dst_port)
        #     # dst_src = dst_ip + " " + src_ip + " " + ip_protocol + " " + str(dst_port) + " " + str(src_port)
        print src_dst
        f.write(src_dst+'\n')
        # f.write(dst_src+'\n')
    f.close()

def dataGenGiveSrcip(src_ip,count):
    f=open('testDataSrcip.txt','a')
    for i in range(count):
        dst_ip = random.choice(ip_address)
        while (src_ip == dst_ip):
            dst_ip = random.choice(ip_address)
        ip_protocol = random.choice(protocol)
        if ip_protocol == '1':
            src_port = ""
            dst_port = ""
        elif ip_protocol == '6':
            src_port = random.choice(tcpPort)
            dst_port = random.randrange(4000, 65500)
        elif ip_protocol == '17':
            src_port = random.choice(udpPort)
            dst_port = random.randrange(4000, 65500)
        if src_port=="":
            src_dst = src_ip + " " + dst_ip + " " + ip_protocol
            # dst_src = dst_ip + " " + src_ip + " " + ip_protocol
        else:
            src_dst = src_ip + " " + dst_ip + " " + ip_protocol + " " + str(src_port) + " " + str(dst_port)
            # dst_src = dst_ip + " " + src_ip + " " + ip_protocol + " " + str(dst_port) + " " + str(src_port)
        print src_dst
        f.write(src_dst+'\n')
        # f.write(dst_src+'\n')
    f.close()



def dataGen(count):
    f = open('testData.txt', 'a')
    for i in range(count):
        src_ip = random.choice(ip_address)
        dst_ip = random.choice(ip_address)
        while (src_ip == dst_ip):
            dst_ip = random.choice(ip_address)
        ip_protocol = random.choice(protocol)
        if ip_protocol == '1':
            src_port = ""
            dst_port = ""
        elif ip_protocol == '6':
            src_port = random.choice(tcpPort)
            dst_port = random.randrange(4000, 65500)
        elif ip_protocol == '17':
            src_port = random.choice(udpPort)
            dst_port = random.randrange(4000, 65500)
        if src_port=="":
            src_dst = src_ip + " " + dst_ip + " " + ip_protocol
            dst_src = dst_ip + " " + src_ip + " " + ip_protocol
        else:
            src_dst = src_ip + " " + dst_ip + " " + ip_protocol + " " + str(src_port) + " " + str(dst_port)
            dst_src = dst_ip + " " + src_ip + " " + ip_protocol + " " + str(dst_port) + " " + str(src_port)
        print src_dst
        f.write(src_dst+'\n')
        f.write(dst_src+'\n')
    f.close()

def loadTestData():
    dataSet=[]
    f=open('testData.txt','r')
    re=f.readlines()
    f.re
    for i in re:
        print i
        print type(i)
        i=i.strip('\n')
        print i.split(" ")
        dataSet.append(i.split(" "))
    return  dataSet
def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = retDict.get(frozenset(trans), 0)+1
    return retDict

if __name__=='__main__':
    # dataGenTcpServcie(50000)
    # redataSet=loadTestData()
    dataGenSrcIpDstIp(50000)
    # # print redataSet
    # print len(redataSet)
    # initSet=createInitSet(redataSet)
    # print len(initSet)
    # print len(initSet.keys())
    # for key in initSet.keys():
    #     if initSet[key]>1:
    #         print key,initSet[key]
    # print initSet
    # dataGen(10000)
