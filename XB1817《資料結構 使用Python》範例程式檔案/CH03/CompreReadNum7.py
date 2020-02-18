#使用List生成式
numB = [] #空的List
numB = [item for item in range(10, 50)if(item % 9 == 0)]
print('10~50被9整除之數：', numB)
