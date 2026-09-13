### Count the number of digits in an integer.

##def get_nos_digits(num: int) -> int:
##    return len(list(str(num)))

def get_nos_digits(num: int) -> int:
    nos_digits=0
    while num>0:
        nos_digits+=1
        num=num//10
    return nos_digits

test_num=12000
print(get_nos_digits(test_num))
        
