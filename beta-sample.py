# %%
import matplotlib.pyplot as plt
from numpy import random
from math import sqrt

def inverseBetaCDF(u):
  return 1 - sqrt(1 - u)

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

u = random.rand(100000)
ax1.hist(u, range=(0.0, 1.0), density=True, bins=10)
ax1.set_ylabel('density')
ax1.set_xlabel('u')

x = list(map(inverseBetaCDF, u))
ax2.hist(x, range=(0.0, 1.0), density=True, bins=10)
ax2.set_ylabel('density')
ax2.set_xlabel('x')
# %%
