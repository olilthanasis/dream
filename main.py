import random, numpy
from matplotlib import pyplot as plt
import numpy as np
lst = []
def single(times):
    drop = 0
    for _ in range(times):
        if random.randint(1,10000)<=473:
            drop+=1
    return drop
sims = 50000000

for i in range(sims):
    if i % 10000 == 0:
        print(f"{(i /sims)*100} %")
    lst.append(single(262))
lst.sort()
dict =[[x,lst.count(x)] for x in set(lst)]
x = list()
y = list()
for i in dict:
   x.append(i[0])
   y.append(i[1])
plt.xlabel("# of simulated ender pearl trades for 262 barters")
plt.ylabel("distribution of values")
plt.title(f"lil's Monte Carlo experiment ({sims} simulations)")
plt.plot(x,y, marker='o')
plt.axvline(x = np.percentile(lst, 50),color ="r")
plt.axvline(x = 42, color ="k")
x1 = nn_percentile = np.percentile(lst, 99)
plt.axvline(x = x1, color ="k")

plt.text(x1,10,'99th percentile',rotation=90)

plt.text(13,0,'median',rotation=90)
plt.text(43,0,"dream's luck",rotation=90)


plt.show()
