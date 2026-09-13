### 25. Find the first repeating character.

import time

def get_first_repeating_char(s: str) -> str:
    temp_set=set()
    for ch in s:
        if ch in temp_set:
            return ch
        else:
            temp_set.add(ch)
    return None



if __name__=="__main__":
    start=time.time()
    temp_str="bcdeae"
    print(get_first_repeating_char(temp_str))
    end=time.time()
    print(f"time consumed--->{(end-start)*1000} ms")
