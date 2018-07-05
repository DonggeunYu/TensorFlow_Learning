import numpy as np

def ReLU(x):
    return np.maximum(0, x)

a = int(input())
print(ReLU(a))