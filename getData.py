import math
import random

# 使用 UUNIFast 算法生成利用率
def getU(n, USum):
    U = []
    sumU = USum
    for i in range(0, n - 1):
        nextSumU = sumU * random.random()**(1 / (n - i))
        U.append(sumU - nextSumU)
        sumU = nextSumU
    U.append(sumU)
    return U

# 生成周期 bound > e
def getT(n, bound):
    T = []
    a = math.log(bound)
    b = 0
    if bound - math.exp(math.floor(a)) <= 0.1:
        b = 1
    i = 0
    while i < a - b - 1:
        for j in range(0, math.floor(n / math.floor(a - b + 1))):
            x = math.exp(i)
            y = math.exp(i + 1)
            T.append(random.uniform(x, y))
        i += 1
    for j in range(0, math.floor(n / math.floor(a - b + 1))):
        x = math.exp(i)
        y = bound
        T.append(random.uniform(x, y))
    left = n % math.floor(a - b + 1)
    for j in range(0, left):
        x = math.exp(j)
        y = math.exp(j + 1)
        T.append(random.uniform(x, y))
    return T

# 生成执行时间，更新利用率
def getC(n, U, T):
    C = []
    UU = []
    for i in range(0, n):
        c = math.floor(T[i] * U[i])
        UU.append(c / T[i])
        C.append(c)
    return C, U

if __name__ == '__main__':
    U = getU(15, 0.85)
    T = getT(15, 100000)
    C, U = getC(15, U, T)
    print('C', C)
    print('U', U)
    print('T', T)