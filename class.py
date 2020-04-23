class FourCal:
    def __init__(self, name, age, univ):
        self.name = name
        self.age = age
        self.univ = univ
        self.add_count = 0
        self.minus_count = 0 
        self.mul_count = 0
        self.div_count = 0 
    
    def add(self, num1 , num2):
        self.add_count += 1 
        return num1 + num2
    def minus(self, num1, num2):
        self.minus_count += 1
        return num1 - num2
    def mul(self, num1, num2):
        self. mul_count += 1
        return num1 * num2
    def div(self, num1, num2):
        if (num2 == 0):
            print('0으로 나눌 수 없습니다')
            return None
        self.div_count += 1 
        return num1 % num2
    def showcount (self): 
        print ("덧셈 : ",  self.add_count)
        print("뺄셈 : ",self.minus_count)
        print("곱셉 : ", self.mul_count)
        print("나눗셈 : ", self.div_count)


calculator1 = FourCal()
calculator1 = FourCal("테일러", 32, "뉴욕대")
print(calculator1.name, calculator1.age, calculator1.univ)