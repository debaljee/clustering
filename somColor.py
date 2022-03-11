import random
import pandas as pd
import matplotlib.pyplot as plt
import sys

class centroid:
    def __init__(self):
        self.x1=-1
        self.x2=-1
        self.x3=-1
    def __init__(self,a,b,c):
        self.x1=a
        self.x2=b
        self.x3=c
class pointVector:
    def __init__(self,a,b,c):
        self.x1=a
        self.x2=b
        self.x3=c
class hyperParameters:
    def __init__(self):
        self.L0=0.9
        self.L1=175
        self.I0=140000
        self.I1=40
        self.maxEpochs=5000
def initCentroids(n):
    centroids=[]
    myCount=0
    count=0
    for i in myData.itertuples():
        if(count==0):
            count+=1
            continue
        centroids.append(centroid(int(i._3),int(i._4),int(i._5)))
        myCount+=1
        if(myCount==n):
            break
    return(centroids)
def eucledianDistance(p1,p2):
    ans=((p1.x1-p2.x1)**2)+((p1.x2-p2.x2)**2)+((p1.x3-p2.x3)**2)
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
        myCentroid[i].x3=myCentroid[i].x3+computeLearningRate(parms,t)*computeInfluenceRate(myCentroid[i],myCentroid[winningCentroid],t)*(myVector.x3-myCentroid[i].x3)
myData=pd.read_csv('color.csv')
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
        destination[i]=centroid(source[i].x1,source[i].x2,source[i].x3)
    return(destination)


for i in range(hyperParameters().maxEpochs):
    oldCentroids=copyCentroids(myCentroid)
    count=0
    for j in myData.itertuples():
        if(count==0):
            count+=1
            continue
        myVector=pointVector(int(j._3),int(j._4),int(j._5))
        nearestCentroid=findNearestCentroid(myCentroid,myVector)
        updateWeights(myCentroid,nearestCentroid,myVector,t)
    if(compareCentroids(oldCentroids,myCentroid)<=0.000000000001):
        break
    t+=1
    print('Evaluating epoch: '+str(t))
myCount=0





def extractColor(colorCentroid):
    myColor='#'
    myColor=myColor+hex(int(colorCentroid.x1))[2:]
    myColor=myColor+hex(int(colorCentroid.x2))[2:]
    myColor=myColor+hex(int(colorCentroid.x3))[2:]
    return(myColor)    


def plotPoint(xPoint,yPoint,nearestCentroid):
    plt.plot(xPoints,yPoints,'o',c=extractColor(myCentroid[nearestCentroid]),ms=2)


def showGrid():
    plt.xticks(fontsize=7)
    plt.yticks(fontsize=7)
    plt.grid(lw=0.1,c='#31783B')

for i in myData.itertuples():
    if(myCount==0):
        myCount+=1
        continue
    myVector=pointVector(int(i._3),int(i._4),int(i._5))
    nearestCentroid=findNearestCentroid(myCentroid,myVector)
    plt.subplot(1,3,1)
    xPoints=[myVector.x1]
    yPoints=[myVector.x2]
    plt.xlabel('Red',fontsize=7)
    plt.ylabel('Green',fontsize=7)
    showGrid() 
    plotPoint(xPoints,yPoints,nearestCentroid)
    plt.subplot(1,3,2)
    xPoints=[myVector.x2]
    yPoints=[myVector.x3]
    plt.xlabel('Green',fontsize=7)
    plt.ylabel('Blue',fontsize=7)
    showGrid()
    plotPoint(xPoints,yPoints,nearestCentroid)
    plt.subplot(1,3,3)
    plt.xlabel('Red',fontsize=7)
    plt.ylabel('Blue',fontsize=7)
    showGrid()
    xPoints=[myVector.x1]
    yPoints=[myVector.x3]
    plotPoint(xPoints,yPoints,nearestCentroid)


if(sys.argv[len(sys.argv)-1]=='showCentroids'):
    for i in range(len(myCentroid)):
        plt.subplot(1,3,1)
        plt.plot([myCentroid[i].x1],[myCentroid[i].x2],'o',c=extractColor(myCentroid[i]),ms=8)
        plt.subplot(1,3,2)
        plt.plot([myCentroid[i].x2],[myCentroid[i].x3],'o',c=extractColor(myCentroid[i]),ms=8)
        plt.subplot(1,3,3)
        plt.plot([myCentroid[i].x1],[myCentroid[i].x3],'o',c=extractColor(myCentroid[i]),ms=8)

plt.suptitle('Clustering using SOM')



plt.show()