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

def int_sqrt_free(N):
    return round(N**0.5)