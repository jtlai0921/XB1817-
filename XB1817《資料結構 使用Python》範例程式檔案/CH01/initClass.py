class Student:
   def __new__(cls, name):   #__new__()建構物件
      if name != '' :
         print('已開始...')
         return object.__new__(cls)
      else:
         print('沒有人報名')
         return None
   def __init__(self, name):   #__init__()初始化物件
      print('報名者：', name)

st1 = Student('') #沒有名稱
st2 = Student('Mary')
