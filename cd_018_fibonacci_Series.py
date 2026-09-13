### Generate the Fibonacci series.

from typing import List

def get_fibonacci(num: int) -> List:
    a, b, c = 0, 1, 0
    fibo_list=[]
    if num>=1:
        fibo_list.append(a)
        return fibo_list
    if num==2:
        fibo_list.append(b)
        return fibo_list
    while num-2>=1:
        c=a+b
        fibo_list.append(c)
        a=b
        b=c
        num-=1
    return fibo_list


def get_fibonacci_series(num:int)->List:
    a, b=0, 1
    fibo_list=[a, b]
    while num-2>0:
        c=a+b
        fibo_list.append(c)
        a=b
        b=c
        num-=1
    return fibo_list
    

test_num=7
print(get_fibonacci(test_num))
