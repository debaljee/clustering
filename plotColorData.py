import sys
import pandas as pd
import matplotlib.pyplot as plt
fileName=sys.argv[1]
showColor=sys.argv[2]
myData=pd.read_csv(fileName,header=None)
def showGrid():
    plt.xticks(fontsize=7)
    plt.yticks(fontsize=7)
    plt.grid(lw=0.1,c='#31783B')

count=0
if(showColor=='showColor'):
    for i in myData.itertuples():
        if(count==0):
            count+=1
            continue
        plt.subplot(1,3,1)
        plt.plot([int(i._3)],[int(i._4)],'o',c=i._2,ms=2)
        plt.xlabel('Red',fontsize=7)
        plt.ylabel('Green',fontsize=7)
        showGrid()
        plt.subplot(1,3,2)
        plt.plot(int(i._4),int(i._5),'o',c=i._2,ms=2)
        plt.xlabel('Green',fontsize=7)
        plt.ylabel('Blue',fontsize=7)    
        showGrid()
        plt.subplot(1,3,3)
        plt.plot(int(i._3),int(i._5),'o',c=i._2,ms=2)
        plt.xlabel('Red',fontsize=7)
        plt.ylabel('Blue',fontsize=7)
        showGrid()
elif(showColor=='hideColor'):
    for i in myData.itertuples():
        if(count==0):
            count+=1
            continue
        plt.subplot(1,3,1)
        plt.plot([int(i._3)],[int(i._4)],'o',c='#F7A400',ms=2)
        plt.xlabel('Red',fontsize=7)
        plt.ylabel('Green',fontsize=7)
        showGrid()
        plt.subplot(1,3,2)
        plt.plot(int(i._4),int(i._5),'o',c='#3A9EFD',ms=2)
        plt.xlabel('Green',fontsize=7)
        plt.ylabel('Blue',fontsize=7)    
        showGrid()
        plt.subplot(1,3,3)
        plt.plot(int(i._3),int(i._5),'o',c='#1A1B4B',ms=2)
        plt.xlabel('Red',fontsize=7)
        plt.ylabel('Blue',fontsize=7)
        showGrid()
plt.suptitle('Color data in RGV plots')

plt.show()