import pandas as pd
myData=pd.read_csv('movie_review.csv')
counter=0
for i,j in myData.iterrows():
    print(j,'\n\n')
    counter+=1
    if(counter==5):
        break