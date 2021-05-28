import matplotlib.pyplot as plt
import numpy as np


t = np.arange(0., 2., 1./180.)*np.pi
plt.polar(t, [7]*len(t))
plt.show()
