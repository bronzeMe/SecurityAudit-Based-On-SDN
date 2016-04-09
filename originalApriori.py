'''

@author: me
'''
from numpy import *
def loadTestData():
    dataSet=[]
    f=open('testDataSrcipII.txt','r')
    re=f.readlines()
    for i in re:
        # print i
        # print type(i)
        i=i.strip('\n')
        # print i.split(" ")
        dataSet.append(i.split(" "))
    return dataSet
def loadDataSet():
    return [['1', '3','4'], ['2', '3', '5'], ['1', '2', '3', '5'], ['2', '5']]


def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat
def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
                
    C1.sort()
    return map(frozenset, C1)#use frozen set so we
                            #can use it as a key in a dict    

def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not ssCnt.has_key(can): ssCnt[can]=1
                else: ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData

def aprioriGen(Lk, k): #creates Ck
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk): 
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            L1.sort(); L2.sort()
            if L1==L2: #if first k-2 elements are equal
                retList.append(Lk[i] | Lk[j]) #set union
    return retList

def apriori(dataSet, minSupport = 0.5):
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)#scan DB to get Lk
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData

def mine_assoc_rules(isets, min_support=0.5, min_confidence=0.5):
    rules = []
    visited = set()
    for key in sorted(isets, key=lambda k: len(k), reverse=True):
        support = isets[key]
        if support < min_support or len(key) < 2:
            continue

        for item in key:
            left = key.difference([item])
            right = frozenset([item])
            _mine_assoc_rules(
                left, right, support, visited, isets,
                min_support, min_confidence, rules)

    return rules


def _mine_assoc_rules(left, right, rule_support, visited, isets, min_support,
        min_confidence, rules):
    if (left, right) in visited or len(left) < 1:
        return
    else:
        visited.add((left, right))

    support_a = isets[left]
    confidence = float(rule_support) / float(support_a)
    if confidence >= min_confidence:
        rules.append((left, right, rule_support, confidence))
        # We can try to increase right!
        for item in left:
            new_left = left.difference([item])
            new_right = right.union([item])
            _mine_assoc_rules(
                new_left, new_right, rule_support, visited, isets,
                min_support, min_confidence, rules)

def generateRules(L,supportData,minSupport=0.5,minConf=0.7):
    isets={}
    for i in range(len(L)):
        for j in L[i]:
            isets[j]=supportData[j]
    rules=mine_assoc_rules(isets,min_support=minSupport,min_confidence=minConf)
    return  rules

def aprioriMain(data,minSupport=0.5,minConf=0.5):
    L,suppData=apriori(data,minSupport)
    rules=generateRules(L,suppData,minSupport,minConf)

    return L,suppData,rules

if __name__=='__main__':
    data=loadTestData()
    L,suppData,rules=aprioriMain(data,0.08,0.5)

    print 'frequent list'
    print len(L)
    #
    print L

    print 'supportData'
    for i in range(len(L)):
        for j in L[i]:
         print j," : ",suppData[j]
         # print
    print 'rules'
    for item in rules:
        print item
    # L,suppData=apriori(data,minSupport=0.5)
    # print L
    # for i in range(len(L)):
    #     for j in L[i]:
    #      print j," :"
    #      print suppData[j]
    # rules=generateRules(L,suppData,minConf=0.5)