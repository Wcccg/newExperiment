import math
import datetime
from readFile import *
from compute import *

if __name__ == '__main__':
    n, sumU, Tmax = readbase('aurg.txt')
    print('\n', 'n = ', n, 'sumU = ', sumU, 'Tmax = ', Tmax)
    C, D, T = readsample('aurg.txt')
    task = readTask('aurg.txt')
    L = getL(C, D, T, sumU, n)
    dmin = getdmin(D, T, n)
    print('dmin = ', dmin)

    print('QPA method:')

    t1 = datetime.datetime.now() - datetime.datetime.now()
    t2 = datetime.datetime.now() - datetime.datetime.now()
    for i in range(0, 100):
        startTime2 = datetime.datetime.now()
        flag2, count2 = useQPA(C, D, T, n, dmin, L)
        endTime2 = datetime.datetime.now()
        t2 += endTime2 - startTime2
        startTime1 = datetime.datetime.now()
        flag1, count1 = useGreaterDistance(task, n, dmin, L)
        endTime1 = datetime.datetime.now()
        t1 += endTime1 - startTime1
    
    print('QPAcount = ', count2, 'time =',  t2)
    print('Discount = ', count1, 'time =',  t1)
    if flag1 == 0:
        print('schedulable')
    else:
        print('unschedulable')
    print('\n')

