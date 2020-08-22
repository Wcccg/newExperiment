import math
import sympy

# L 即 Tbound
def getL(C, D, T, sumU, n):
    La = getLa(C, D, T, sumU, n)
    Lb = getLb(C, T, n)
    if sumU == 1:
        return Lb
    else:
        return min(La, Lb)

def getLa(C, D, T, sumU, n):
    La = -1
    m = 0
    for i in range(0, n):
        La = max(La, D[i])
        m = m + (T[i] - D[i]) * C[i] / T[i]
    m = m / (1 - sumU)
    La = max(La, m)
    return La

def getLb(C, T, n):
    x0 = 0
    x1 = -1
    for i in range(0, n):
        x0 = x0 + C[i]
    while x0 != x1:
        x1 = x0
        x0 = 0
        for i in range(0, n):
            x0 = x0 + math.ceil(x1 / T[i]) * C[i]
    Lb = x0
    return Lb

# 计算处理器需求函数
def getH(t, C, D, T, n):
    H = 0
    for i in range(0, n):
        h = max(0, 1 + math.floor((t - D[i]) / T[i])) * C[i]
        H = H + h
    return H

# 计算总上界函数
def getUpBound(t, C, D, T, n):
    uB = 0
    for i in range(0, n):
        ub = C[i] / T[i] * (t - D[i]) + C[i]
        uB = uB + ub
    return uB

# 返回上界函数参数
def getB(t, C, D, T, n):
    a = 0
    b = 0
    for i in range(0, n):
        a += (0 if ((t - D[i]) % T[i] != 0 or t < D[i]) else C[i] / T[i])
        b += (max(0, 1 + math.floor((t - D[i]) / T[i])) * C[i] if ((t - D[i]) % T[i] != 0 or t < D[i]) else C[i] - C[i] * D[i] / T[i])
    return a, b

# 获取 dmin
def getdmin(D, T, n):
    dmin = 1000000
    for i in range(0, n):
        dmin = min(dmin, D[i])
    return dmin

# 获取距离 X 最近的拐点，没有则返回 -1
def getdmax(X, D, T, n):
    dmax = -1
    for i in range(0, n):
        m = int(X / T[i]) * T[i] + D[i]
        while m >= X:
            if m >= T[i] + D[i]:
                m = m - T[i]
            else:
                m = -1
        dmax = max(dmax, m)
    return dmax

# 同时返回该拐点编号
def getdmax2(X, D, T, n):
    dmax = -1
    index = 0
    for i in range(0, n):
        m = int(X / T[i]) * T[i] + D[i]
        while m >= X:
            if m >= T[i] + D[i]:
                m = m - T[i]
            else:
                m = -1
        if m > dmax:
            dmax = m
            index = i
    return dmax, i

# 使用 QPA 算法进行跳转
def useQPA(C, D, T, n, dmin, L):
    print('L = ', L)
    count = 0       # 记录跳转次数
    t = getdmax(L, D, T, n)
    h = getH(t, C, D, T, n)
    while (h <= t and h > dmin):
        count = count + 1
        if h < t:
            t = h
        else:
            t = getdmax(t, D, T, n)
            if t == -1:
                return 1, count
        h = getH(t, C, D, T, n)
    if h <= dmin:       # 可调度返回 0
        return 0, count
    else:               # 不可调度返回 1 
        return 1, count 

# 使用上界线思路进行跳转
def useUpBound(C, D, T, n, dmin, L, sumU):
    count = 0       # 记录跳转次数
    Dmax = -1
    for i in range(0, n):
        Dmax = max(Dmax, D[i])
    # 区间优化
    origin = getUpBound(Dmax, C, D, T, n)
    if origin <= Dmax:
        L = min(L, Dmax)
    else:
        l = 0
        for i in range(0, n):
            l = l - C[i] * D[i] / T[i] + C[i]
        l = l / (1 - sumU)
        L = min(L, l)
    # 坐标跳转
    print('L = ', L)
    tt = getdmax(L, D, T, n)
    a, b = getB(tt, C, D, T, n)
    t = b / (1 - a)
    while (t <= tt and t > dmin):
        count = count + 1
        tt = int(t)
        tt = getdmax(tt, D, T, n)
        if tt == -1:
            return 1, count
        a, b = getB(tt, C, D, T, n)
        t = b / (1 - a)
        print('tt = ', tt, 't = ', t)
    if t <= dmin:       # 可调度返回 0
        return 0, count
    else:               # 不可调度返回 1 
        return 1, count 
    