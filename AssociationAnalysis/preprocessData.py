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
f=open('testDataTcp.txt','r')
data=f.readlines()
datalist=[]
for item in data:
    itemtmp=item.strip("\n").split(" ")
    # print itemtmp
    ele=tranfrom(itemtmp)
    # print "____________"
    # print ele
    datalist.append(ele)
# print datalist
X=datalist
X = StandardScaler().fit_transform(X)
print 'after standard x'
print X
db = DBSCAN(eps=0.5, min_samples=10).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)# init a zero anarry [false,false...]x
# core_samples_mask[db.codbre_sample_indices_] = True
labels = db.labels_
print 'type labels'
print type(labels)
print 'core_samples_mask'
print core_samples_mask
print len(core_samples_mask)
print 'labels[0-9]'
print labels[:10]
print labels[11:20]
labelstest=labels[200:300]
print labelstest
testmp=(1 if -1 in labelstest else 0)
print 'testmp'
print testmp
settest=set(labels)
print 'set test'
print settest
#
# # Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)# cluster id begin with 0--
#
print 'Number of clusters'
print n_clusters_
cluster_dict={}
for i in range(n_clusters_):
    cluster_dict[i]=[]

for i in range(len(labels)):
    if labels[i]==-1:
        pass
    else:
        cluster_dict[labels[i]].append(datalist[i])
f=open('DBSCAN_result.txt','w')
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
        print tranfromToRawData(subitem)
        f.write(str(tranfromToRawData(subitem))+"\n")
# f.close()
f.write('predict one new data \n')
f.write(str(datalist[:50]))
f.write("\n")
Y = StandardScaler().fit_transform([[0,3,4]])
result=db.fit_predict(Y)
# result=DBSCAN(eps=0.5, min_samples=10).fit_predict(Y)
f.write('predict result:\n')
f.write(str(result))
f.close()