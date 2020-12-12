#기본 계산기
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b !=0:
        return a/b
    else:
        return 'ZeroDivisionError'

def square(n):
    return n**2

#여기까지가 기본적인 수학 함수입니다.