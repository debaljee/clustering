import matplotlib.pyplot as plt
import pandas as pd
def xAxis():
    xPoints=[i for i in range(4,8)]
    yPoints=[0 for i in range(4,8)]
    plt.subplot(1,2,1)
    plt.plot(xPoints,yPoints,lw=0.5,c='#CED93B')
    plt.grid(lw=0.1,c='#31783B')
    plt.xticks(fontsize=7)
    plt.yticks(fontsize=7)
    plt.xlabel('x axis',fontsize=7)
    plt.ylabel('y axis',fontsize=7)
    plt.title('First graph')
    plt.subplot(1,2,2)
    plt.plot(xPoints,yPoints,lw=0.5,c='#CED93B')
    plt.grid(lw=0.3,c='#31783B')
    plt.xticks(fontsize=7)
    plt.yticks(fontsize=7)
    plt.xlabel('x axis',fontsize=7)
    plt.ylabel('y axis',fontsize=7)
    plt.title('Second Graph')

def yAxis():
    xPoints=[4 for i in range(0,8)]
    yPoints=[i for i in range(0,8)]
    plt.subplot(1,2,1)
    plt.plot(xPoints,yPoints,lw=0.5,c='#CED93B')

myData=pd.read_csv('iris.csv')
minSepal=9999999.999999
maxSepal=-9999999.99999
minPetal=99999999.9999999
maxPetal=-999999999.9999999
for i in myData.itertuples():
    plt.subplot(1,2,1)
    xPoint=[i.SepalLengthCm]
    yPoint=[i.PetalLengthCm]
    plt.plot(xPoint,yPoint,'o',c='#4E7C91',ms=1)
    print(i)

xAxis()
yAxis()
plt.show()