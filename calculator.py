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
def get_remainder(a,b):
    return a//b
def get_abs(n):
    return abs(n)
def get_Percent(a,b):
    return (a/b)*100
