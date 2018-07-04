import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = 0
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NOR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0
    tmp = np.sum(x*w) + b
    if tmp < 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    x = NAND(x1, x2)
    y = OR(x1, x2)
    return AND(x, y)

print('1. AND')
print('2. NAND')
print('3. OR')
print('4. NOR')

a = input()

b, c = input().split()
b = b(int)
c = c(int)
if(a == 1):
    print(AND(b, c))
if(a == 2):
    print(NAND(b, c))
if(a == 3):
    print(OR(b, c))
if(a == 4):
    print(NOR(b, c))