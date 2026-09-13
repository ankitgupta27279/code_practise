### Reverse an integer without converting it to a string.

def get_reverse_integer(num: int) -> int:
    rev_num=0
    while num>0:
        rev_num=(rev_num*10)+(num%10)
        num=num//10
    return rev_num


test_num=123
print(get_reverse_integer(test_num))