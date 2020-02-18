#第五章實作(二)-8，以遞廻方式將List的元素反轉
def reverse(num, start, stop):
   if start < (stop - 1):
      num[start], num[stop - 1] = num[stop - 1], num[start]
      reverse(num, start + 1, stop - 1)
      return num

data = [2, 5, 12, 8, 6, 7, 9]
data = reverse(data, 0, 7)
print(data)