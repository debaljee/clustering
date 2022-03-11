import sys
import random
import matplotlib.pyplot as plt

class constants:
    def __init__(self):
        self.r=0.3



def determineRank(vect):
    arr=[char for char in vect]
    count=1
    for i in range(len(arr)):
        if(arr[i]==','):
            count+=1
    return(count)

def eucledianDistance(v1,v2):
    sum=0
    for i in range(len(v1)):
        sum=sum+(v1[i]-v2[i])*(v1[i]-v2[i])
    sum=sum**(0.5)
    return(sum)

def extractVector(item):
    arr=[char for char in item]
    mySubstring=''
    myVector=[]
    for i in range(1,len(arr)):
        if(arr[i]!=',' and arr[i]!=']'):
            mySubstring=mySubstring+arr[i]
        else:
            myVector.append(float(mySubstring))
            mySubstring=''
    return(myVector)


myCentroids=[]
for i in range(1,len(sys.argv)-1):
    myCentroids.append(extractVector(sys.argv[i]))

xVector=[]
yVector=[]
zVector=[]
rank=determineRank(sys.argv[1])
for i in range(len(myCentroids)):
    xVector.append(myCentroids[i][0])
    yVector.append(myCentroids[i][1])
    if(rank==3):
        zVector.append(myCentroids[i][2])
print(xVector)
print(yVector)
print(rank)
for i in range(len(myCentroids)):
    myR=constants()
    myR.r=float(sys.argv[len(sys.argv)-1])
    myCircle=plt.Circle([myCentroids[i][0],myCentroids[i][1]],myR.r,fill=False,color='#3A9EFD',lw=0.5)
    fig=plt.gcf()
    axes=fig.gca()
    axes.add_patch(myCircle)



myFile=open('userData.csv','w')
def scatterRandomly(myCentroids):
    for i in range(len(myCentroids)):
        myCount=1
        while(myCount<=100):
            myR=constants()
            myR.r=float(sys.argv[len(sys.argv)-1])
            randomNum1=random.randrange(-1000,1000)
            randomNum2=random.randrange(-1000,1000)
            xi=(randomNum1/1000)*myR.r
            yi=(randomNum2/1000)*myR.r
            if((xi**2+yi**2)<myR.r**2):
                plt.plot([xi+myCentroids[i][0]],[yi+myCentroids[i][1]],'o',c='#F7A400',ms=2)                
                myStr=''
                myStr=myStr+str(xi+myCentroids[i][0])+','
                myStr=myStr+str(yi+myCentroids[i][1])
                myFile.write(myStr)
                myFile.write('\n')
                myCount+=1



scatterRandomly(myCentroids)
if(rank==2):
    plt.plot(xVector,yVector,'o',c='#1A1B4B',ms=2)


plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.grid(lw=0.1,c='#31783B')
plt.title('plot',fontsize=7)
myFile.close()
plt.show()
