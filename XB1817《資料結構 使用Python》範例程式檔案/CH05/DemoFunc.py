#簡單的遞廻函式
def showNum(n):
  if n > 0 :
    print(n)
    showNum(n-1)

showNum(4)