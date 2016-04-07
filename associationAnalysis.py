import loadMySqlData
import originalApriori
import originalFPgrowth

data=loadMySqlData.loadDataFromDB('userlog',('src_ip','dst_ip','service','dpid','port'))
datalist=loadMySqlData.preprocessData(data)
print datalist
for item in datalist:
    print item


frequentApri,suppDataApri,rulesApri=originalApriori.aprioriMain(data,0.3,0.5)
frequentFP,suppDataFP,rulesFP=originalFPgrowth.fpgrowthMain(data,0.3,0.5)

print 'frequent list Apri'
for item in frequentApri:
    print item

print 'frequent list FP'
for item in frequentFP:
    print item

print 'rules given by Apri'
for item in rulesApri:
    print item

print 'rules given by FP-growth'
for item in rulesFP:
    print item





