import matplotlib.pyplot as plt
import pandas as pd
myData=pd.read_csv('meanSquaredDistance.csv',header=None)
xValues=[]
yValues=[]
for i in myData.itertuples():
    xValues.append(i._1)
    yValues.append(i._2)
plt.plot(xValues,yValues,lw=0.5,c='#1A1B4B')
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.grid(lw=0.1,c='#31783B')
plt.ylabel('Mean squared distance from nearest centroid',fontsize=7)
plt.xlabel('Number of clusters',fontsize=7)


plt.show()