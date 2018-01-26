# this is an idea to explain p-values
import numpy as np
from scipy import stats

x = np.linrange(-3,3,100)
p = stats.norm.pdf(x)
p = p/np.sum(p)
a = 1.96
stats.norm.pdf(0)




