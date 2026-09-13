### 24. Find the first non-repeating character.

import time
from collections import Counter


def get_first_non_repeating_char_1(s: str) -> str:
    temp_list=set()
    is_non_repeating=None
    for i in range(0, len(s)):
        is_non_repeating=True
        for j in range(i+1, len(s)):
            if s[i]==s[j] or s[i] in temp_list:
                is_non_repeating=False
                temp_list.add(s[i])
                break
        if is_non_repeating and s[i] not in temp_list:
            return s[i]
    return None


def get_first_non_repeating_char_2(s: str) -> str:
    for ch in s:
        if s.count(ch)==1:
            return ch
    return None


def get_first_non_repeating_char_3(s: str) -> str:
    count=Counter(s)
    for ch in s:
        if count[ch]==1:
            return ch
    return None

def get_first_non_repeating_char_4(s: str) -> str:
    ch_freq={}
    for ch in s:
        ch_freq[ch]=ch_freq.get(ch, 0)+1
    for ch in s:
        if ch_freq[ch]==1:
            return ch
    return None


if __name__=="__main__":
    start=time.time()
    # test_str="abcdbcda"
    # test_str="abcdbcdae"
    test_str="fabcdadbc"
    print(get_first_non_repeating_char_4(test_str))
    end=time.time()
    print(f"time consumed--->{(end-start)*1000}")
