#ploting the graph


import matplotlib.pyplot as plt

x=[]
y=[]

plt.scatter(x,y,label='reg',color='k')

plt.xlabel('words')

plt.ylabel('bhm-25')
plt.title('logistic regression (classification) problem')

plt.legend()
plt.show()
