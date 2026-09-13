### Find the factorial of a number (iterative and recursive).

def get_factorial_iterative(num: int) -> int:
   if num>=0:
       num_fact=1
       while num>0:
           num_fact*=num
           num-=1
       return num_fact
   else:
       print(f"{num} is less than 0, factorial not possible.")
       return None


def get_factorial_recursive(num: int) -> int:
    if num<0:
        print(f"{num} is less than 0, factorial not possible.")
        return None
    elif num==0:
        return 1
    else:
        return num*get_factorial_recursive(num-1)


# print(get_factorial_iterative(-1))
print(get_factorial_recursive(3))
