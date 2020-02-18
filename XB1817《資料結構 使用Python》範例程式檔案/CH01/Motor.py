#定義類別 -- 利用方法來取得屬性並做輸出

class Motor:
    
    #定義方法一：取得名稱和顏色
    def buildCar(self, name, color):
        self.name = name
        self.color = color
        
    #定義方法二：輸出名稱和顏色
    def showMessage(self):
        print('款式:{0:6s}, 顏色:{1:4s}'.format(
           self.name, self.color))

# 產生物件
car1 = Motor()#物件1
car1.buildCar('Vios', '極光藍')
car1.showMessage() #呼叫方法

car2 = Motor()#物件2
car2.buildCar('Altiss', '炫魅紅')
car2.showMessage()