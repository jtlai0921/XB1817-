#找出10~50之間被7整除的數值
numA = [] #空的List
for item in range(10, 50):
    if(item % 7 == 0):
        numA.append(item) #整除的數放入List中
print('10~50被7整除之數：', numA)
