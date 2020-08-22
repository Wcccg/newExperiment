import math
import datetime
from readFile import *
from compute import *

if __name__ == '__main__':
    n, sumU, Tmax = readbase('aurg.txt')
    C, D, T = readsample('aurg.txt')
    L = getL(C, D, T, sumU, n)
    dmin = getdmin(D, T, n)
    print('dmin = ', dmin, '\n')

    print('QPA method:')
    startTime1 = datetime.datetime.now()
    flag1, count1 = useQPA(C, D, T, n, dmin, L)
    endTime1 = datetime.datetime.now()
    if flag1 == 0:
        print('schedulable')
    else:
        print('unschedulable')
    print('count = ', count1)
    print('time=', endTime1 - startTime1)
    print('\nupBound method:')

    startTime2 = datetime.datetime.now()
    flag2, count2 = useUpBound(C, D, T, n, dmin, L, sumU)
    endTime2 = datetime.datetime.now()
    if flag2 == 0:
        print('schedulable')
    else:
        print('unschedulable')
    print('count = ', count2)
    print('time=', endTime2 - startTime2, '\n')
