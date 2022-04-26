# import libraries
import numpy as np
import random as r
import pandas as pd

# import data
data = pd.read_csv('people.csv')

# this example are for 3 clusters
c1 = []
c2 = []
c3 = []

# named height and weight from data
a1 = data['height'] 
a2 = data['weight']

# every row of data is added to new array
df = [] 
for i in range(len(data)):
    df.append([a1[i],a2[i]])

# choose random 3 centers
n1=r.choice(df)
n2=r.choice(df)
while n2==n1:
    n2 = r.choice(df)
n3=r.choice(df) 
while n1==n3 or n2==n3:
    n3=r.choice(df) 
print(' First center',n1,'\n','Second center',n3,'\n','Third center',n3,'\n')


# all distances 
all_c1 =[]
all_c2 =[]
all_c3 =[]

# find the centroids which points are closest, add points to appropriate class
for i in df:
    d1 = np.sqrt(np.power(i[0]-n1[0],2)+np.power(i[1]-n1[1],2))
    all_c1.append(d1)

    d2 = np.sqrt(np.power(i[0]-n2[0],2)+np.power(i[1]-n2[1],2))
    all_c2.append(d2)

    d3 = np.sqrt(np.power(i[0]-n3[0],2)+np.power(i[1]-n3[1],2))
    all_c3.append(d3)

    if min(d1,d2,d3)==d1:
        c1.append(i)

    if min(d1,d2,d3)==d2:
        c2.append(i)

    if min(d1,d2,d3)==d3:
        c3.append(i)

# show all distances with data
centr = pd.DataFrame({'height':a1,'weight':a2,'c1':all_c1,'c2':all_c2,'c3':all_c3})
print(centr)

# calculate new centroids
def findSum(arr):
    sum1, sum2 = 0,0
    for i in arr:
        sum1 += i[0]
        sum2 += i[1]
    return [(sum1/len(arr)),(sum2/len(arr))]
sum_c1 = findSum(c1)
sum_c2 = findSum(c2)
sum_c3 = findSum(c3)

# calculate sum of new classes
sums = pd.DataFrame([sum_c1,sum_c2,sum_c3],index=['c1','c2','c3'],columns=['A1','A2'])
print('\n',sums)
