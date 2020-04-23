# 홀수단(1,3,5,7,9단) 출력하는 함수 gugudan_odd 함수 정의
# 짝수단(2,4,6,8단) 출력하는 함수 gugudan_even 함수 정의
# 인자가 홀수면 gugudan_odd 함수를 실행, 짝수면 gugudan_even 함수를 실행하는 함수 gugudan_odd_or_even 함수 정의 및 실행

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