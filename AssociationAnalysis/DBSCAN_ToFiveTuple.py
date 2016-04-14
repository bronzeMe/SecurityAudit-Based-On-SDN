import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

ip_address = ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4', '10.0.0.5',
              '10.0.0.6', '10.0.0.7', '10.0.0.8', '10.0.0.9', '10.0.0.10']

tcpUsualService=['http','telnet','icmp','smtp','https','ssh','ftp']

ip_address_index={}
id_ip_address={}
id_tcpUsualService={}
tcpUsualService_index={}
id=0
for item in ip_address:
    ip_address_index[item]=id
    id_ip_address[id]=item
    id+=1

# for item in ip_address_index:
#     print item,ip_address_index[item]

id=0
for item in tcpUsualService:
    tcpUsualService_index[item]=id
    id_tcpUsualService[id]=item
    id+=1

# for item in tcpUsualService_index:
#     # print 's'
#     print item,tcpUsualService_index[item]

def preprocessData(data):
    ele=[]
    ele.append(ip_address_index[data[0]])
    ele.append(ip_address_index[data[1]])
    ele.append(eval(data[2]))
    if len(data)==3:
        ele.append(0)
        ele.append(0)
    else:
        ele.append(eval(data[3]))
        ele.append(eval(data[4]))
    return ele

def loadDataFromFile(filename):
    f=open(filename,'r')
    datalist=[]
    data=f.readlines()
    for item in data:
        itemtmp=item.strip("\n").strip("\r").split(" ")
        ele=preprocessData(itemtmp)
        datalist.append(ele)
    return datalist

def transfromToRawFiveTuple(data):
    ele=[]
    ele.append(id_ip_address[data[0]])
    ele.append(id_ip_address[data[1]])
    # if len(data)==3:
    ele.append(data[2])
    # else:
    ele.append(data[3])
    ele.append(data[4])
    return ele



def tranfrom(data):
    ele=[]
    ele.append(ip_address_index[data[0]])
    ele.append(ip_address_index[data[1]])
    if len(data)>2:
        ele.append(tcpUsualService_index[data[2]])
    return ele
def tranfromToRawData(data):
    ele=[]
    ele.append(id_ip_address[data[0]])
    ele.append(id_ip_address[data[1]])
    if len(data)>2:
        ele.append(id_tcpUsualService[data[2]])
    return  ele

def getDistance(X,Y):
    length=len(X)
    tmp=0
    for i in range(length):
        tmp+=(X[i]-Y[i])**2
    return tmp**(0.5)
if __name__=='__main__':
    datalist=loadDataFromFile('testData.txt')
    for item in datalist:
        print item
    #------compute DBSCAN algorithm
    X=datalist
    Y=StandardScaler().fit_transform(X)#must execute Standard to get more prefect result
    db=DBSCAN(eps=0.2,min_samples=5).fit(Y)

    labels=db.labels_
    # # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)# cluster id begin with 0--
    print 'Number of clusters'
    print n_clusters_
    cluster_dict={}
    cluster_coresample={}
    for i in range(n_clusters_):
        cluster_dict[i]=[]
        cluster_coresample[i]=[]
    #
    for i in range(len(labels)):
        if labels[i]==-1:
            pass
        else:
            cluster_dict[labels[i]].append(datalist[i])
            cluster_coresample[labels[i]].append(Y[i])
    f=open('DBSCAN_result_five.txt','w')
    f.write(str(n_clusters_))
    f.write('\n')
    for item in cluster_dict:
        f.write("cluster: ")
        f.write(str(item))
        f.write(": length: ")
        f.write(str(len(cluster_dict[item])))
        f.write("\n")
        print item,":","length:",len(cluster_dict[item])
        for subitem in cluster_dict[item]:
            print subitem
            f.write(str(subitem)+": ")
            print transfromToRawFiveTuple(subitem)
            f.write(str(transfromToRawFiveTuple(subitem))+"\n")

    newrecord='10.0.0.1 10.0.0.4 17 68 33403'
    newrecordattack='10.0.0.1 10.0.0.4 17 1090 8080'
    newrecordlist=preprocessData(newrecord.split(" "))
    attacklist=preprocessData(newrecordattack.split(" "))
    f.write("newrecord \n")
    f.write(str(newrecord.split(" ")))
    f.write("predict result \n")

    # datalist=loadDataFromFile('testData.txt')
    datalist.append(newrecordlist)
    # recordlist.append(newrecordlist)
    print 'new record'
    print newrecordlist
    newrecordX=StandardScaler().fit_transform(datalist)
    print 'new record standard'
    print newrecordX[-1]
    newrecordtopredict=newrecordX[-1]
    for key in cluster_coresample:
        # itemlist=[]
        item=cluster_coresample[key][0]#get core sample
        # print "core sample"
        # print item
        # itemlist.append(item)
        # itemstandard=StandardScaler().fit_transform(itemlist)
        # print 'standard core sample'
        # print itemstandard
        distance=getDistance(newrecordtopredict,item)
        if distance<=0.2:
            print 'distance'
            print distance
            f.write(str(key))
            break
    #
    #
    # # result=db.fit_predict(newrecordX)
    # # f.write(str(result))
    # f.close()

    # f.write('predict one new data \n')
    # f.write(str(datalist[:50]))
    # f.write("\n")
    # Y = StandardScaler().fit_transform([[0,3,4]])
    # result=db.fit_predict(Y)
    # # result=DBSCAN(eps=0.5, min_samples=10).fit_predict(Y)
    # f.write('predict result:\n')
    # f.write(str(result))
    # f.close()
# X=datalist
# X = StandardScaler().fit_transform(X)
# print 'after standard x'
# print X
# db = DBSCAN(eps=0.5, min_samples=10).fit(X)
# core_samples_mask = np.zeros_like(db.labels_, dtype=bool)# init a zero anarry [false,false...]x
# # core_samples_mask[db.codbre_sample_indices_] = True
# labels = db.labels_
# print 'type labels'
# print type(labels)
# print 'core_samples_mask'
# print core_samples_mask
# print len(core_samples_mask)
# print 'labels[0-9]'
# print labels[:10]
# print labels[11:20]
# labelstest=labels[200:300]
# print labelstest
# testmp=(1 if -1 in labelstest else 0)
# print 'testmp'
# print testmp
# settest=set(labels)
# print 'set test'
# print settest
# #
# # # Number of clusters in labels, ignoring noise if present.
# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)# cluster id begin with 0--
# #
# print 'Number of clusters'
# print n_clusters_
# cluster_dict={}
# for i in range(n_clusters_):
#     cluster_dict[i]=[]
#
# for i in range(len(labels)):
#     if labels[i]==-1:
#         pass
#     else:
#         cluster_dict[labels[i]].append(datalist[i])
# f=open('DBSCAN_result.txt','w')
# f.write(str(n_clusters_))
# f.write('\n')
# for item in cluster_dict:
#     f.write("cluster: ")
#     f.write(str(item))
#     f.write(": length: ")
#     f.write(str(len(cluster_dict[item])))
#     f.write("\n")
#     print item,":","length:",len(cluster_dict[item])
#     for subitem in cluster_dict[item]:
#         print subitem
#         f.write(str(subitem)+": ")
#         print tranfromToRawData(subitem)
#         f.write(str(tranfromToRawData(subitem))+"\n")
# # f.close()
# f.write('predict one new data \n')
# f.write(str(datalist[:50]))
# f.write("\n")
# Y = StandardScaler().fit_transform([[0,3,4]])
# result=db.fit_predict(Y)
# # result=DBSCAN(eps=0.5, min_samples=10).fit_predict(Y)
# f.write('predict result:\n')
# f.write(str(result))
# f.close()