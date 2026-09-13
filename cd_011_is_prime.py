### 11. Check if a number is prime.

def is_prime(num: int) -> bool:
    if num<2:
        return False
    for i in range(2, num):
        if num%i==0:
            return False
    return True

def is_prime(num: int):
    if num==2:
        return True
    elif num<=1:
        return False
    else:
        for i in range(2, num):
            if num%i==0:
                return False
        return True


test_num=119
print(is_prime(test_num))
