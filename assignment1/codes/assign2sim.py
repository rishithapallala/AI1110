import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
#import seaborn as sns
#Number of tosses
n = 4 
#Probability of a head
p = 1/2
#k is the possible values of the heads
k_values = list(range(n+1))
#y gives the probability values for each of the values of k
y = binom.pmf(k_values,n,p)
z=[y[0],y[1],y[2],y[3],y[4]]
print(z)   #printing the probability of different number of heads after 4 tosses
#Simulating the probability using the binomial random variable
simlen = 10000
data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of a coin tossed 4 times and noting the number of heads
total_count = [np.count_nonzero(data_binom == 0)/simlen,np.count_nonzero(data_binom == 1)/simlen,np.count_nonzero(data_binom == 2)/simlen,np.count_nonzero(data_binom == 3)/simlen,np.count_nonzero(data_binom == 4)/simlen]

print(total_count)  #printing the probability of getting different number of heads based on the simulation


