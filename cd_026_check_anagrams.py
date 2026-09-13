### 26. Check if two strings are anagrams.

def is_anagram_1(s1: str, s2: str) -> bool:
    # set comparison
    # ts1=set(s1)
    # ts2=set(s2)
    # print(f"ts1--->{ts1}")
    # print(f"ts2--->{ts2}")
    # return True if ts1==ts2 else False
    return True if set(s1)==set(s2) else False ### only works if there is no repeating char in strings like aaafz and aafz


######## this is wrong - STARTED ########
# def is_anagram_2(s1: str, s2: str) -> bool:
#     # using dictionary comparison
#     dict1=dict2={}
#     for c in s1:
#         dict1[c]=dict.get(c, 0)+1
#     for c in s2:
#         dict2[c]=dict.get(c, 0)+1
#     return True if dict1==dict2 else False
######## this is wrong - END ########

def is_anagram_2(s1: str, s2: str)->bool:
    if len(s1)==len(s2):
        dict1={}
        dict2={}
        for i in range(len(s1)):
            dict1[s1[i]]=dict1.get(s1[i], 0)+1
            dict2[s2[i]]=dict2.get(s2[i], 0)+1
        return True if dict1==dict2 else False
    else:
        return False

def is_anagram_3_using_sorted(s1: str, s2: str) -> bool:
    # using string comparison
    new_s1="".join(sorted(s1))
    new_s2="".join(sorted(s2))
    return True if new_s1==new_s2 else False

def is_anagram_using_sort(s1: str, s2: str) -> bool:
    #using list comparison
    l1=list(sorted(list(s1)))
    l2=list(sorted(list(s2)))
    return True if l1==l2 else False




if __name__=="__main__":
    # str1="tapan"
    # str2="patan"
    str1="ankit"
    str2="tikna"
    print(is_anagram_using_sort(str1, str2))
