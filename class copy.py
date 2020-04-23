class FourCal:
    def __init__(self, name, age, univ):
        self.name = name
        self.age = age
        self.univ = univ
    
    def add(self, num1 , num2):
        return num1 + num2
    def minus(self, num1, num2):
        return num1 - num2
    def mul(self, num1, num2):
        return num1 * num2
    def div(self, num1, num2):
        if (num2 == 0):
            print('0으로 나눌 수 없습니다')
            return None
        return num1 % num2


calculator1 = FourCal()
calculator1 = FourCal("테일러", 24, "캠브릿지")
print(calculator1.name, calculator1.age, calculator1.univ)