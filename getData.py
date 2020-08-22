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
            T.append(int(random.uniform(x, y)))
        i += 1
    for j in range(0, math.floor(n / math.floor(a - b + 1))):
        x = math.exp(i)
        y = bound
        T.append(int(random.uniform(x, y)))
    left = n % math.floor(a - b + 1)
    for j in range(0, left):
        x = math.exp(j)
        y = math.exp(j + 1)
        T.append(int(random.uniform(x, y)))
    return T


# 生成执行时间，更新周期和利用率
def getC(n, U, T):
    C = []
    newT = []
    sumU = 0
    for i in range(0, n):
        u = random.uniform(0.0001, 0.0005)
        u = max(U[i], u)
        c = T[i] * u
        if c > 1:
            c = math.floor(c)
        else:
            c = math.ceil(c)
        t = math.ceil(c / u)
        sumU += c / t
        C.append(c)
        newT.append(t)
    return C, newT, sumU


# 生成deadline
def getD(n, C, T):
    D = []
    for i in range(0, n):
        if C[i] < 10:
            a = C[i]
        elif C[i] < 100 and C[i] >= 10:
            a = 2 * C[i]
        elif C[i] < 1000 and C[i] >= 100:
            a = 3 * C[i]
        else:
            a = 4 * C[i]
        b = 1.2 * T[i]
        D.append(int(random.uniform(a, b)))
    return D


# 保存数据至文本文件
def writefile(filename, C, D, T, n, sumU, Tmax):
    with open(filename, 'w') as f:
        lens = len(C)
        f.write(str(n) + ' ' + str(round(sumU, 5)) + ' ' + str(Tmax) + '\n')
        for i in range(0, lens):
            temp = round(U[i], 5)
            stri = str(C[i]) + ' ' + str(D[i]) + ' ' + str(T[i]) + '\n'
            f.write(stri)

if __name__ == '__main__':
    n = 1000
    sumU = 0.90
    Tmax = 10000
    U = getU(n, sumU)
    T = getT(n, Tmax)
    C, T, sumU = getC(n, U, T)
    D = getD(n, C, T)
    writefile('aurg.txt', C, D, T, n, sumU, Tmax)
