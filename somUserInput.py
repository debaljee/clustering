import random
import matplotlib.pyplot as plt
import pandas as pd
import sys

inputArray=[]

inputArray=[]
fileName=sys.argv[1]
myData=pd.read_csv(fileName,header=None)
for i in myData.itertuples():
    inputArray.append([i._1,i._2])

class centroid:
    def __init__(self):
        self.x1=-1
        self.x2=-1
    def __init__(self,a,b):
        self.x1=a
        self.x2=b
class pointVector:
    def __init__(self,a,b):
        self.x1=a
        self.x2=b
class hyperParameters:
    def __init__(self):
        self.L0=0.9
        self.L1=175
        self.I0=140000
        self.I1=40
def initCentroids(n):
    centroids=[]
    myCount=0
    for i in myData.itertuples():
        centroids.append(centroid(i._1,i._2))
        myCount+=1
        if(myCount==n):
            break
    return(centroids)
def eucledianDistance(p1,p2):
    ans=((p1.x1-p2.x1)**2)+((p1.x2-p2.x2)**2)
    ans=ans**(0.5)
    return(ans)
def findNearestCentroid(myCentroid,myVector):
    n=len(myCentroid)
    min=999999999999.99999999
    minIndex=-1
    for i in range(n):
        if(eucledianDistance(myVector,myCentroid[i])<min):
            minIndex=i
            min=eucledianDistance(myVector,myCentroid[i])
    return(minIndex)
def computeLearningRate(myParameters,t):
    ans=(myParameters.L0)*(2.718281828**(-t/myParameters.L1))
    return(ans)
def computeInfluence(myParameters,t):
    ans=(myParameters.I0)*(2.718281828**(-t/myParameters.I1))
    return(ans)
def computeInfluenceRate(vector1,vector2,t):
    myDistance=eucledianDistance(vector1,vector2)
    parms=hyperParameters()
    myInfluenceRate=computeInfluence(parms,t)
    myDistance=myDistance*myDistance
    myDistance=-myDistance
    myInfluenceRate=myInfluenceRate*myInfluenceRate
    myInfluenceRate=myInfluenceRate*2
    ans=2.718281828**(myDistance/myInfluenceRate)
    return(ans)
def updateWeights(myCentroid,winningCentroid,myVector,t):
    parms=hyperParameters()
    for i in range(len(myCentroid)):
        myCentroid[i].x1=myCentroid[i].x1+computeLearningRate(parms,t)*computeInfluenceRate(myCentroid[i],myCentroid[winningCentroid],t)*(myVector.x1-myCentroid[i].x1)
        myCentroid[i].x2=myCentroid[i].x2+computeLearningRate(parms,t)*computeInfluenceRate(myCentroid[i],myCentroid[winningCentroid],t)*(myVector.x2-myCentroid[i].x2)

t=0

myCentroid=initCentroids(int(sys.argv[len(sys.argv)-2]))

def compareCentroids(oldCentroids,newCentroids):
    sum=0
    for i in range(len(oldCentroids)):
        sum=sum+eucledianDistance(oldCentroids[i],newCentroids[i])
    sum=sum/len(oldCentroids)
    return(sum)
def copyCentroids(source):
    destination=[None for i in range(len(source))]
    for i in range(len(destination)):
        destination[i]=centroid(source[i].x1,source[i].x2)
    return(destination)

for i in range(5000):
    oldCentroids=copyCentroids(myCentroid)
    for j in range(len(inputArray)):
        myVector=pointVector(inputArray[j][0],inputArray[j][1])
        nearestCentroid=findNearestCentroid(myCentroid,myVector)
        updateWeights(myCentroid,nearestCentroid,myVector,t)
    if(compareCentroids(oldCentroids,myCentroid)<=0.0000000000000001):
        break
    t+=1
    print('Evaluating epoch: '+str(t))

def xAxis():
    xPoints=[i for i in range(0,9)]
    yPoints=[0 for i in range(0,9)]
    plt.plot(xPoints,yPoints,lw=0.5,c='#3E4491')
    plt.xticks(fontsize=7)
    plt.yticks(fontsize=7)
    plt.grid(lw=0.1,c='#31783B')
def yAxis():
    xPoints=[0 for i in range(0,9)]
    yPoints=[i for i in range(0,9)]
    plt.plot(xPoints,yPoints,lw=0.5,c='#3E4491')

'''
xAxis()
yAxis()
'''


for i in range(len(inputArray)):
    myVector=pointVector(inputArray[i][0],inputArray[i][1])
    nearestCentroid=findNearestCentroid(myCentroid,myVector)
    xPoints=[myVector.x1]
    yPoints=[myVector.x2]
    if(nearestCentroid==0):
        plt.plot(xPoints,yPoints,'o',c='#F7A400',ms=4)
    if(nearestCentroid==1):
        plt.plot(xPoints,yPoints,'o',c='#3A9EFD',ms=4)
    if(nearestCentroid==2):
        plt.plot(xPoints,yPoints,'o',c='#1A1B4B',ms=4)
    if(nearestCentroid==3):
        plt.plot(xPoints,yPoints,'o',c='yellow',ms=4)
    if(nearestCentroid==4):
        plt.plot(xPoints,yPoints,'o',c='green',ms=4)
    if(nearestCentroid==5):
        plt.plot(xPoints,yPoints,'o',c='red',ms=4)


if(sys.argv[len(sys.argv)-1]=='showCentroids'):
    for i in range(len(myCentroid)):
         plt.plot([myCentroid[i].x1],[myCentroid[i].x2],'o',c='black')

plt.suptitle('Clustering using SOM algorithm on User Dataset')
plt.show()
