class Father: #基底類別一
    def walking(self):
        print('多走路有益健康!')

class Mother: #基底類別二
    def riding(self):
        print('I can ride a bike!')

class Son(Father, Mother): #衍生類別
    pass

Joe = Son()   #產生子類別實體
Joe.walking()
Joe.riding()
