from typing import Any

# def is_pallindrome(data: Any) -> bool:
#     is_pallin=False
#     data_list=list(str(data))
#     rev_data_list=list(reversed(data_list))
#     print(f"data_list--->{data_list}")
#     print(f"rev_data_list--->{rev_data_list}")
#     if data_list == rev_data_list:
#         is_pallin = True
#     return is_pallin

def is_palindrome(num:int)->bool:
    temp_num=num
    new_num=0
    while num>0:
        new_num=(new_num*10)+(num%10)
        num=num//10
    return True if new_num==temp_num else False

def is_pallindrome(data: Any) -> bool:
    return True if list(str(data)) == list(str(data))[::-1] else False
        


test_num=12321
# test_data="racecar"
test_data="welcome"
print(is_pallindrome(test_num))
# print(is_pallindrome(test_data))