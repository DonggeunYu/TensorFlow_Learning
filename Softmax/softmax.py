import numpy as np

a = np.array([1100, 1000, 1010])
c = np.max(a)
print(np.exp(a - c) / np.sum(np.exp(a - c)))