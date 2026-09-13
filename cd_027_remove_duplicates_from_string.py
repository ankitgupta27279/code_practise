### 27. Remove duplicate characters from a string.


def remove_duplicate_chars_1(s: str) -> str:
    return "".join(set(s))

def remove_duplicate_chars_2(s: str) -> str:
    temp_list=[]
    for ch in s:
        if ch not in temp_list:
            temp_list.append(ch)
    return "".join(temp_list)

########## only keeping elements whose frequency is 1 and removing all others - STARTED #########
def remove_duplicates_2(s: str)->str:
    return "".join([ch for ch in s if s.count(ch)==1])

def remove_duplicates_3(s: str)->str:
    temp_list=[]
    count=Counter(s)
    for ch in s:
        if count[ch]==1:
            temp_list.append(ch)
    return "".join(temp_list)

def remove_duplicates_4(s: str)->str:
    temp_dict={}
    temp_list=[]
    for ch in s:
        temp_dict[ch]=temp_dict.get(ch, 0)+1
    for ch in s:
        if temp_dict[ch]==1:
            temp_list.append(ch)
    return "".join(temp_list)
########## only keeping elements whose frequency is 1 and removing all others - END #########


if __name__=="__main__":
    test_str="fabcdabcde"
    print(remove_duplicate_chars_2(test_str))
