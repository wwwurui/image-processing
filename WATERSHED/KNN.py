from numpy import *
import operator

def creatData():
    group=array([[0,0],[1.0,1.1],[1.0,1.0,],[0,0.1]])
    label=["A","B","B","A"]
    return group,label

def classify0 (inX,dataSet,labels,k):
    dataSetSize= dataSet.shape[0]
    difMat=tile(inX,(dataSetSize,1))-dataSet
    sqdifMat=difMat**2
    sqDistance=sqdifMat.sum(axis=1)
    Distance=sqDistance**0.5
    sortDistance=Distance.argsort()
    classCount={}
    for i in range(k):
        voteLabels=labels[sortDistance[i]]
        classCount[voteLabels]=classCount.get(voteLabels,0)+1
        sortClasscount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortClasscount[0][0]

group,labels=creatData()
print (group)
print (labels)
class_label=classify0([0,0],group,labels,3)
print (class_label)
