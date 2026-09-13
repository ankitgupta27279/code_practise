# def get_all_duplicate_elements(nums: List) -> List:
#     duplicate_list=[]
#     new_list=[]
#     for num in nums:
#         if num not in new_list:
#             new_list.append(num)
#         else:
#             duplicate_list.append(num)
#     return duplicate_list

def get_all_duplicate_elements(nums: List) -> List:
    duplicate_list=[]
    i=0
    while i<len(nums):
        j=i+1
        while j<len(nums):
            if nums[i]==nums[j]:
                duplicate_list.append(nums.pop(j))
            else:
                j+=1
        i+=1
    return duplicate_list


def get_duplicates(nums: List):
    dict_freq={}
    list_dup=[]
    for num in nums:
        dict_freq[num]=dict_freq.get(num, 0)+1
    for key in dict_freq.keys():
        if dict_freq[key]>1:
            list_dup.append(key)
    return list_dup


test_list=[7, 1, 7, 3, 5, 8, 3, 2, 1, 9, 9]
print(get_all_duplicate_elements(test_list))