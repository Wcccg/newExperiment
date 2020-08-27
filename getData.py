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
def getT(n, bound, Tmin):
    n -= 1
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
            T.append(int(random.uniform(x, y)) * Tmin)
        i += 1
    for j in range(0, math.floor(n / math.floor(a - b + 1))):
        x = math.exp(i)
        y = bound
        T.append(int(random.uniform(x, y)) * Tmin)
    left = n % math.floor(a - b + 1)
    for j in range(0, left):
        x = math.exp(j)
        y = math.exp(j + 1)
        T.append(int(random.uniform(x, y)) * Tmin)
    T.append(int(bound * Tmin))
    return T


# 生成执行时间，更新周期和利用率
def getC(n, U, T, Tmax, Tmin):
    C = []
    newT = []
    sumU = 0
    for i in range(0, n):
        u = U[i]
        # u = max(u, 1 / Tmax)
        # u = min(u, 1 / Tmin)
        c = T[i] * u
        if c > 1:
            c = math.floor(c)
        else:
            c = math.ceil(c)
        t = math.floor(c / u)
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
        f.write(str(n) + ' ' + str(round(sumU, 5)) + ' ' + str(max(T)) + ' ' + str(min(T)) + '\n')
        for i in range(0, lens):
            stri = str(C[i]) + ' ' + str(D[i]) + ' ' + str(T[i]) + '\n'
            f.write(stri)

def getTmax(n, sumU, mul):
    u = sumU / n
    Tmin = int(0.5 / u)
    Tmax = int(Tmin * mul)
    return Tmax, Tmin

if __name__ == '__main__':
    n = 30
    sumU = 0.85
    mul = 10            # Tmax / Tmin
    Tmax, Tmin = getTmax(n, sumU, mul)
    print(Tmax, Tmin)
    U = getU(n, sumU)
    T = getT(n, mul, Tmin)
    C, T, sumU = getC(n, U, T, Tmax, Tmin)
    D = getD(n, C, T)
    # print(Tmax, Tmin)
    # print(max(T), min(T), sumU, max(T) / min(T))
    writefile('aurg.txt', C, D, T, n, sumU, Tmax)
