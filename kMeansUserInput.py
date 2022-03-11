import random
import matplotlib.pyplot as plt
import pandas as pd
import sys
class constants:
    def __init__(self):
        self.numberOfCentroids=5



inputArray=[]
fileName=sys.argv[1]
myData=pd.read_csv(fileName,header=None)
for i in myData.itertuples():
    inputArray.append([i._1,i._2])
class centroid:
    def __init__(self):
        self.x1=-1
        self.x2=-1
        self.x1sum=0
        self.x2sum=0
        self.cumulative=0
    def __init__(self,a,b):
        self.x1=a
        self.x2=b
        self.x1sum=0
        self.x2sum=0
        self.cumulative=0
class pointVector:
    def __init__(self,a,b):
        self.x1=a
        self.x2=b
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

myCentroid=initCentroids(int(sys.argv[len(sys.argv)-2]))
t=0
for p in range(5000):
    for i in range(len(inputArray)):
        myVector=pointVector(inputArray[i][0],inputArray[i][1])
        nearestCentroid=findNearestCentroid(myCentroid,myVector)
        myCentroid[nearestCentroid].x1sum=myCentroid[nearestCentroid].x1sum+myVector.x1
        myCentroid[nearestCentroid].x2sum=myCentroid[nearestCentroid].x2sum+myVector.x2
        myCentroid[nearestCentroid].cumulative=myCentroid[nearestCentroid].cumulative+1
    oldCentroids=copyCentroids(myCentroid)
    for i in range(len(myCentroid)):
        myCentroid[i].x1sum=myCentroid[i].x1sum+myCentroid[i].x1
        myCentroid[i].x2sum=myCentroid[i].x2sum+myCentroid[i].x2
        myCentroid[i].cumulative=myCentroid[i].cumulative+1
        myCentroid[i].x1=myCentroid[i].x1sum/myCentroid[i].cumulative
        myCentroid[i].x2=myCentroid[i].x2sum/myCentroid[i].cumulative
        myCentroid[i].cumulative=0
        myCentroid[i].x1sum=0
        myCentroid[i].x2sum=0
    if(compareCentroids(oldCentroids,myCentroid)<=0.00000000000000001):
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
meanSquaredDistance=float(0)
countTuples=0
for i in range(len(inputArray)):
    countTuples=countTuples+1
    myVector=pointVector(inputArray[i][0],inputArray[i][1])
    nearestCentroid=findNearestCentroid(myCentroid,myVector)
    distance=eucledianDistance(myCentroid[nearestCentroid],myVector)
    distance=distance*distance
    meanSquaredDistance=meanSquaredDistance+distance    
    xPoints=[myVector.x1]
    yPoints=[myVector.x2]
    if(nearestCentroid==0):
        plt.plot(xPoints,yPoints,'o',c='#F7A400',ms=3)
    if(nearestCentroid==1):
        plt.plot(xPoints,yPoints,'o',c='#3A9EFD',ms=3)
    if(nearestCentroid==2):
        plt.plot(xPoints,yPoints,'o',c='#1A1B4B',ms=3)
    if(nearestCentroid==3):
        plt.plot(xPoints,yPoints,'o',c='yellow',ms=3)
    if(nearestCentroid==4):
        plt.plot(xPoints,yPoints,'o',c='green',ms=3)
    if(nearestCentroid==5):
        plt.plot(xPoints,yPoints,'o',c='red',ms=3)

meanSquaredDistance=meanSquaredDistance/countTuples
myFile=open('meanSquaredDistance.csv','a')
myString=str(int(sys.argv[len(sys.argv)-2]))+','+str(meanSquaredDistance)+'\n'
myFile.write(myString)

plt.suptitle('Clustering using K means algorithm on User Dataset')
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
if(sys.argv[len(sys.argv)-1]=='showCentroids'):
    for i in range(len(myCentroid)):
         plt.plot([myCentroid[i].x1],[myCentroid[i].x2],'o',c='black')

plt.grid(lw=0.1,c='#31783B')
plt.show()
