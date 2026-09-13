# def get_list_after_removing_duplicates(nums: List) -> List:
#     return list(set(nums))


def get_list_after_removing_duplicates(nums: List) -> List:
    new_list=[]
    for num in nums:
        if num not in new_list:
            new_list.append(num)
    return new_list

def remove_duplicates_from_list_1(nums):
    test_set=set()
    for num in nums:
        if num not in test_set:
            test_set.add(num)
    return list(test_set)


# def get_list_after_removing_duplicates_same_list(nums: List) -> List:
#     i=0
#     while i<len(nums):
#         j=i+1
#         while j<len(nums):
#             if nums[i] == nums[j]:
#                 nums.pop(j)
#             else:
#                 j+=1
#         i+=1
#     return nums

def get_list_after_removing_duplicates_same_list(nums: List) -> List:
    i=0
    while i<len(nums):
        j=i+1
        while j<len(nums):
            if nums[i]==nums[j]:
                nums.pop(j)
            else:
                j+=1
        i+=1
    return nums



test_list=[7, 1, 7, 3, 5, 8, 3, 2, 1, 9, 9, 2]
# test_list=[2, 1, 2]
# print(get_list_after_removing_duplicates(test_list))
print(get_list_after_removing_duplicates_same_list(test_list))