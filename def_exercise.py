# def iseven (number):
#     if (number %2 == 0):
#         print('짝수')
#     else :
#         print('홀수')

def gugudan_odd():
    for i in range (1,10,2):
        for j in range(1,10):
            print (f'{i}x{j}={i*j}')


def iseven2(number):
    if (number %2 == 0):
        gugudan_odd()
    else: 
        print('홀수')

iseven2(4)





#아래는 내가 한게 아니고# 
def gugudan (num) : 
    if (num % 2 == 0) :
        i = 2 
        while i < 10:
            for j in range (1,10):
                print ("%d * %d" % (i,j))




class FourCal: 
    def add(self, n1, n2):
        result = n1 + n2 
        return result

a = FourCal()

calculator1 = FourCal ()
print (calculator1.add(3,4))

class FourCal:
    def _init_ (self, name, age):
        self.name = name
        self.age = age

calculator = FourCal ("테일러", 24)
print

