import sys
import pandas as pd
import matplotlib.pyplot as plt

fileName=sys.argv[1]
myData=pd.read_csv(fileName,header=None)
for i in myData.itertuples():
    plt.plot([i._1],[i._2],'o',c='#1A1B4B',ms=2)

plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.grid(lw=0.1,c='#31783B')

plt.show()