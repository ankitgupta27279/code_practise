### 12. Print all prime numbers in a given range-excluding both start & end.

def get_all_prime_nos(start: int, end: int) -> List:
    prime_nos=[]
    is_prime=None
    if start>=0 and end>start+1:
        for i in range(start+1, end):
            is_prime=True
            if i==2:
                prime_nos.append(i)
                continue
            for j in range(2, i):
                if i%j == 0:
                    is_prime=False
                    break
            if is_prime:
                prime_nos.append(i)
    else:
        print("No prime nos in this range")
        return
    return prime_nos


def get_prime_in_range(start: int, end: int):
    prime_list=[]
    for i in range(start, end+1):
        is_prime=True
        if i==1:
            continue
        else:
            for j in range(2, i):
                if i%j==0:
                    is_prime=False
                    break
            if is_prime:
                prime_list.append(i)
    return prime_list


print(get_all_prime_nos(2,58))
        
