Q2. 인자에 따라 홀수 구구단(1,3,5,7,9단) 또는 짝수 구구단(2,4,6,8단)을 출력하는 함수 작성 및 실행 

# def odd_or_even (num):
#     if (num %2 == 0):
#         print (홀수 구구단)
#     else : 
#         print (짝수 구구단)


def gugudan_odd():
    for i in range (1,10,2):
        for j in range(1,10):
            print (f'{i}x{j}={i*j}')


def gugudan_even():
    for i in range (2,10,2):
        for j in range(1,10):
            print (f'{i}x{j}={i*j}'')


def gugudan_odd_or_even (num):
    if(num % 2 ==0):
        gugudan_even()
    else:
        gugudan_odd()

gugudan_odd_or_even(1)