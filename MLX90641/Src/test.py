def judge(pointList):
    list = pointList
    diff = 0
    for i in list:
        if not i == 0:
            diff += (list[i] - list[i - 1])
    print("diff: ", diff)


pointList = [1,2,3,4,5,6]

