 = datetime.datetime.now()
    flag1, count1 = useQPA(C, D, T, n, dmin, L)
    endTime1 = datetime.datetime.now()
    if flag1 == 0:
        print('schedulable')
    else:
        print('unschedulable')
    print('count = ', count1)
    print('time=', endTime1 - startTime1)