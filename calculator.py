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

#여기까지가 기본적인 수학 함수입니다.

#연습용으로 만든 피보나치 수열 코드입니다.
def fibbonachi_zero_one_calls(num_list):
    dynamic_list = [[1,0],[0,1]]
    for i in range(2,max(num_list)+1):
        dynamic_list.append([dynamic_list[i-1][0]+dynamic_list[i-2][0], dynamic_list[i-1][1]+dynamic_list[i-2][1]])
    
    res_str = ""
    for n in num_list:
        res_str += f"{dynamic_list[n][0]} {dynamic_list[n][1]}"
        res_str += "\n"

    return res_str