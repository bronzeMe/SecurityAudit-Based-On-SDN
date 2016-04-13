from pymining import itemmining
from pymining import seqmining
from pymining import assocrules,perftesting
import originalApriori
import originalFPgrowth
transactions=perftesting.get_default_transactions()
transactions=(('1', '3','4'), ('2', '3', '5'), ('1', '2', '3', '5'), ('2', '5'))
print 'transactions'
for item in transactions:
    print item
relim_input=itemmining.get_relim_input(transactions)
print 'relim_input'
print relim_input
# report=itemmining.relim(relim_input,min_support=2)
# print report
transactionslist=[]
for item in transactions:
    tmplist=[]
    for i in item:
        tmplist.append(i)
    transactionslist.append(tmplist)
# transactionslist=[['a','b','c'],['b'],['a'],['a','c','d'],['b','c'],['b','c']]
# seqs=('caabc','abcb','cabc','abbca')
print 'transactionslist'
transactionslist=[['1', '3','4'], ['2', '3', '5'], ['1', '2', '3', '5'], ['2', '5']]
for item in transactionslist:
    print item
# freq_seqs=seqmining.freq_seq_enum(seqs,min_support=2)
# print sorted(freq_seqs)

print 'assocrules'
item_sets=itemmining.relim(relim_input,min_support=2)
print 'his frequent itemset'
# pri(item_sets)nt type
for i in item_sets:
    print i,": ",item_sets[i]
rules=assocrules.mine_assoc_rules(item_sets,min_support=2,min_confidence=0.5)
for i in rules:
    print i

l,suppdata,rules=originalApriori.aprioriMain(transactionslist,minSupport=0.5,minConf=0.5)
print 'my apriori frequent itemset'
# for i in l:
#     print i,": ",suppdata[i]
print 'my apriori rules'
for item in rules:
    print item



lf,suppFdata,rules=originalFPgrowth.fpgrowthMain(transactionslist,minSupport=0.5,minConf=0.5)
print 'my fp frequent itemset'
for i in lf:
    print i
# for i in l:
#     print i,": ",suppdata[i]
print 'my fp rules'
for item in rules:
    print item
