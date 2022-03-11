import random
import pandas as pd
import sys
import matplotlib.pyplot as plt

class centroid:
    def __init__(self):
        self.x1=-1
        self.x2=-1
        self.x3=-1
        self.x4=-1
        self.x1sum=0
        self.x2sum=0
        self.x3sum=0
        self.x4sum=0
        self.cumulative=0
    def __init__(self,a,b,c,d):
        self.x1=a
        self.x2=b
        self.x3=c
        self.x4=d
        self.x1sum=0
        self.x2sum=0
        self.x3sum=0
        self.x4sum=0
        self.cumulative=0

class pointVector:
    def __init__(self,a,b,c,d):
        self.x1=a
        self.x2=b
        self.x3=c
        self.x4=d

def initCentroids(n):
    centroids=[]
    myCount=0
    for i in myData.itertuples():
        centroids.append(centroid(i.SepalLengthCm,i.SepalWidthCm,i.PetalLengthCm,i.PetalWidthCm))
        myCount+=1
        if(myCount==n):
            break
    return(centroids)


def eucledianDistance(p1,p2):
    ans=((p1.x1-p2.x1)**2)+((p1.x2-p2.x2)**2)+((p1.x3-p2.x3)**2)+((p1.x4-p2.x4)**2)
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


myData=pd.read_csv('iris.csv')
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
        destination[i]=centroid(source[i].x1,source[i].x2,source[i].x3,source[i].x4)
    return(destination)


for i in range(5000):
    for j in myData.itertuples():
        myVector=pointVector(j.SepalLengthCm,j.SepalWidthCm,j.PetalLengthCm,j.PetalWidthCm)
        nearestCentroid=findNearestCentroid(myCentroid,myVector)
        myCentroid[nearestCentroid].x1sum=myCentroid[nearestCentroid].x1sum+myVector.x1
        myCentroid[nearestCentroid].x2sum=myCentroid[nearestCentroid].x2sum+myVector.x2
        myCentroid[nearestCentroid].x3sum=myCentroid[nearestCentroid].x3sum+myVector.x3
        myCentroid[nearestCentroid].x4sum=myCentroid[nearestCentroid].x4sum+myVector.x4
        myCentroid[nearestCentroid].cumulative=myCentroid[nearestCentroid].cumulative+1
    oldCentroids=copyCentroids(myCentroid)
    for i in range(len(myCentroid)):
        myCentroid[i].x1sum=myCentroid[i].x1sum+myCentroid[i].x1
        myCentroid[i].x2sum=myCentroid[i].x2sum+myCentroid[i].x2
        myCentroid[i].x3sum=myCentroid[i].x3sum+myCentroid[i].x3
        myCentroid[i].x4sum=myCentroid[i].x4sum+myCentroid[i].x4
        myCentroid[i].cumulative=myCentroid[i].cumulative+1
        myCentroid[i].x1=myCentroid[i].x1sum/myCentroid[i].cumulative
        myCentroid[i].x2=myCentroid[i].x2sum/myCentroid[i].cumulative
        myCentroid[i].x3=myCentroid[i].x3sum/myCentroid[i].cumulative
        myCentroid[i].x4=myCentroid[i].x4sum/myCentroid[i].cumulative
        myCentroid[i].cumulative=0
        myCentroid[i].x1sum=0
        myCentroid[i].x2sum=0
        myCentroid[i].x3sum=0
        myCentroid[i].x4sum=0        
    if(compareCentroids(oldCentroids,myCentroid)<=0.00000000001):
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
plt.subplot(2,3,1)
xAxis()
yAxis()
plt.xlabel('Sepal length in cm',fontsize=7)
plt.ylabel('Petal length in cm',fontsize=7)
plt.subplot(2,3,2)
xAxis()
yAxis()
plt.xlabel('Sepal length in cm',fontsize=7)
plt.ylabel('Petal width in cm',fontsize=7)
plt.subplot(2,3,3)
xAxis()
yAxis()
plt.xlabel('Sepal length in cm',fontsize=7)
plt.ylabel('Sepal width in cm',fontsize=7)

plt.subplot(2,3,4)
xAxis()
yAxis()
plt.xlabel('Petal length in cm',fontsize=7)
plt.ylabel('Sepal width in cm',fontsize=7)
plt.subplot(2,3,5)
xAxis()
yAxis()
plt.xlabel('Petal length in cm',fontsize=7)
plt.ylabel('Petal width in cm',fontsize=7)
plt.subplot(2,3,6)
xAxis()
yAxis()
plt.xlabel('Petal width in cm',fontsize=7)
plt.ylabel('Sepal width in cm',fontsize=7)



def plotPoint(xPoint,yPoint,nearestCentroid):
    if(nearestCentroid==0):
        plt.plot(xPoints,yPoints,'o',c='#F7A400',ms=2)
    if(nearestCentroid==1):
        plt.plot(xPoints,yPoints,'o',c='#3A9EFD',ms=2)
    if(nearestCentroid==2):
        plt.plot(xPoints,yPoints,'o',c='#1A1B4B',ms=2)
    if(nearestCentroid==3):
        plt.plot(xPoints,yPoints,'o',c='yellow',ms=2)
    if(nearestCentroid==4):
        plt.plot(xPoints,yPoints,'o',c='green',ms=2)
    if(nearestCentroid==5):
        plt.plot(xPoints,yPoints,'o',c='red',ms=2)

meanSquaredDistance=float(0)
countTuples=0
for i in myData.itertuples():
    countTuples=countTuples+1
    myVector=pointVector(i.SepalLengthCm,i.SepalWidthCm,i.PetalLengthCm,i.PetalWidthCm)
    nearestCentroid=findNearestCentroid(myCentroid,myVector)
    distance=eucledianDistance(myCentroid[nearestCentroid],myVector)
    distance=distance*distance
    meanSquaredDistance=meanSquaredDistance+distance
    plt.subplot(2,3,1)
    xPoints=[myVector.x1]
    yPoints=[myVector.x3]
    plotPoint(xPoints,yPoints,nearestCentroid)
    plt.subplot(2,3,2)
    xPoints=[myVector.x1]
    yPoints=[myVector.x4]
    plotPoint(xPoints,yPoints,nearestCentroid)
    plt.subplot(2,3,3)
    xPoints=[myVector.x1]
    yPoints=[myVector.x2]
    plotPoint(xPoints,yPoints,nearestCentroid)
    plt.subplot(2,3,4)
    xPoints=[myVector.x3]
    yPoints=[myVector.x2]
    plotPoint(xPoints,yPoints,nearestCentroid)
    plt.subplot(2,3,5)
    xPoints=[myVector.x3]
    yPoints=[myVector.x4]
    plotPoint(xPoints,yPoints,nearestCentroid)
    plt.subplot(2,3,6)
    xPoints=[myVector.x4]
    yPoints=[myVector.x2]
    plotPoint(xPoints,yPoints,nearestCentroid)
meanSquaredDistance=meanSquaredDistance/countTuples
myFile=open('meanSquaredDistance.csv','a')
myString=str(int(sys.argv[len(sys.argv)-2]))+','+str(meanSquaredDistance)+'\n'
myFile.write(myString)
plt.subplot(2,3,1)
xValue=[i.x1 for i in myCentroid]
yValue=[i.x3 for i in myCentroid]
plt.suptitle('Clustering using K means algorithm')
if(sys.argv[len(sys.argv)-1]=='showCentroids'):
    for i in range(len(myCentroid)):
        plt.subplot(2,3,3)
        plt.plot([myCentroid[i].x1],[myCentroid[i].x2],'o',c='black',ms=2.5)
        plt.subplot(2,3,2)
        plt.plot([myCentroid[i].x1],[myCentroid[i].x4],'o',c='black',ms=2.5)
        plt.subplot(2,3,1)
        plt.plot([myCentroid[i].x1],[myCentroid[i].x3],'o',c='black',ms=2.5)
        plt.subplot(2,3,4)
        plt.plot([myCentroid[i].x3],[myCentroid[i].x2],'o',c='black',ms=2.5)
        plt.subplot(2,3,5)
        plt.plot([myCentroid[i].x3],[myCentroid[i].x4],'o',c='black',ms=2.5)
        plt.subplot(2,3,6)
        plt.plot([myCentroid[i].x4],[myCentroid[i].x2],'o',c='black',ms=2.5)


plt.show()
