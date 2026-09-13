def get_smallest(nums: List) -> int:
    return min(nums) if len(nums)>0 else None

# def get_smallest(nums: List) -> int:
#     if len(nums)<1:
#         print("empty list")
#         return None
#     first=float('inf')
#     for num in nums:
#         if num<first:
#             first=num
#     return first
def get_smallest(test_list):
    smallest=float('inf')
    for num in test_list:
        if num<smallest:
            smallest=num
    return smallest
    
def get_smallest_1(test_list):
    return sorted(test_list)[0]

def get_smallest_2(test_list):
    test_list.sort()
    return test_list[0]

def get_smallest_3(test_list):
    return min(test_list)


# test_list=[5, 1, 16, 8, 2, 12, 3]
# test_list=[5]
# test_list=[]
test_list=[5, 7, 5, 8]
print(get_smallest(test_list))