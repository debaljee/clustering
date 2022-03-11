import matplotlib.pyplot as plt
import pandas as pd
myData=pd.read_csv('iris.csv')
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




for i in myData.itertuples():
    print(i)
    plt.subplot(2,3,1)
    xPoints=[i.SepalLengthCm]
    yPoints=[i.PetalLengthCm]
    if(i.Species=='Iris-virginica'):
        plt.plot(xPoints,yPoints,'o',c='#F7A400',ms=2)
    elif(i.Species=='Iris-setosa'):
        plt.plot(xPoints,yPoints,'o',c='#3A9EFD',ms=2)
    else:
        plt.plot(xPoints,yPoints,'o',c='#1A1B4B',ms=2)
    plt.subplot(2,3,2)
    xPoints=[i.SepalLengthCm]
    yPoints=[i.PetalWidthCm]
    if(i.Species=='Iris-virginica'):
        plt.plot(xPoints,yPoints,'o',c='#F7A400',ms=2)
    elif(i.Species=='Iris-setosa'):
        plt.plot(xPoints,yPoints,'o',c='#3A9EFD',ms=2)
    else:
        plt.plot(xPoints,yPoints,'o',c='#1A1B4B',ms=2)
    plt.subplot(2,3,3)
    xPoints=[i.SepalLengthCm]
    yPoints=[i.SepalWidthCm]
    if(i.Species=='Iris-virginica'):
        plt.plot(xPoints,yPoints,'o',c='#F7A400',ms=2)
    elif(i.Species=='Iris-setosa'):
        plt.plot(xPoints,yPoints,'o',c='#3A9EFD',ms=2)
    else:
        plt.plot(xPoints,yPoints,'o',c='#1A1B4B',ms=2)
    plt.subplot(2,3,4)
    xPoints=[i.PetalLengthCm]
    yPoints=[i.SepalWidthCm]
    if(i.Species=='Iris-virginica'):
        plt.plot(xPoints,yPoints,'o',c='#F7A400',ms=2)
    elif(i.Species=='Iris-setosa'):
        plt.plot(xPoints,yPoints,'o',c='#3A9EFD',ms=2)
    else:
        plt.plot(xPoints,yPoints,'o',c='#1A1B4B',ms=2)
    plt.subplot(2,3,5)
    xPoints=[i.PetalLengthCm]
    yPoints=[i.PetalWidthCm]
    if(i.Species=='Iris-virginica'):
        plt.plot(xPoints,yPoints,'o',c='#F7A400',ms=2)
    elif(i.Species=='Iris-setosa'):
        plt.plot(xPoints,yPoints,'o',c='#3A9EFD',ms=2)
    else:
        plt.plot(xPoints,yPoints,'o',c='#1A1B4B',ms=2)
    plt.subplot(2,3,6)
    xPoints=[i.PetalWidthCm]
    yPoints=[i.SepalWidthCm]
    if(i.Species=='Iris-virginica'):
        plt.plot(xPoints,yPoints,'o',c='#F7A400',ms=2)
    elif(i.Species=='Iris-setosa'):
        plt.plot(xPoints,yPoints,'o',c='#3A9EFD',ms=2)
    else:
        plt.plot(xPoints,yPoints,'o',c='#1A1B4B',ms=2)
plt.show()