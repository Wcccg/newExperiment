import math
import sympy

# L 即 Tbound
def getL(U, C, D, T, sU, n):
    La = getLa(U, D, T, su, n)
    Lb = getLb(C, T, n)
    if sU == 1:
        return Lb
    else:
        return min(La, Lb)

def getLa(U, D, T, su, n):
    La = -1
    m = 0
    for i in range(0, n):
        La = max(La, D[i])
        m = m + (T[i] - D[i]) * U[i]
    m = m / (1 - sU)
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

# 获取某一坐标下的上界函数
def getB(tt, t, C, D, T, n):
    B = 0
    for i in range(0, n):
        if (tt - D[i]) % T[i] != 0 or tt < D[i]:
            b = max(0, 1 + math.floor((tt - D[i]) / T[i])) * C[i]
        else:
            b = C[i] / T[i] * (t - D[i]) + C[i]
        B = B + b
    return B

# 获取 dmin
def getdmin(L, D, T, n):
    dmin = 1000000
    for i in range(0, n):
        dmin = min(dmin, D[i])
    return dmin

# 获取距离 X 最近的拐点
def getdmax(X, D, T, n):
    dmax = -1
    for i in range(0, n):
        m = int(X / T[i]) * T[i] + D[i]
        if m >= X and m >= T[i]:
            m = m - T[i]
        dmax = max(dmax, m)
    return dmax

# 使用 QPA 算法进行跳转
def useQPA(C, D, T, n, dmin, dmax):
    count = 0       # 记录跳转次数
    t = getdmax(L, D, T, n)
    h = getH(t, C, D, T, n)
    while (h <= t and h > dmin):
        count = count + 1
        if h < t:
            t = h
        else:
            t = getdmax(t, D, T, n)
        h = getH(t, C, D, T, n)
    if h <= dmin:       # 可调度返回 0
        return 0, count
    else:               # 不可调度返回 1 
        return 1, count 

# 使用上界线思路进行跳转
def useUpBound(C, D, T, n, dmin, L, U):
    count = 0       # 记录跳转次数
    t = sympy.Symbol('t')
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
            l = l + C[i] * D[i] / T[i] - C[i]
        l = l / (1 - U)
        L = min(L, l)
    # 坐标跳转
    tt = getdmax(L, D, T, n)
    h = getH(tt, C, D, T, n)
    while h <= t and h > dmin:
        count = count + 1
        b = getB(tt, t, C, D, T, n)
        tt = sympy.solve(b - t, t)[0]
        tt = getdmax(tt, D, T, n)
        h = getH(tt, C, D, T, n)
    if h <= dmin:       # 可调度返回 0
        return 0, count
    else:               # 不可调度返回 1 
        return 1, count 
    