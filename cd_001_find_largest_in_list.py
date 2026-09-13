# def get_largest(nums: List) -> int:
#     return max(nums) if len(nums)>0 else None


def get_largest(nums: list) -> int:
    if len(nums)<1:
        print("empty list")
        return None
    first=float('-inf')
    for num in nums:
        if num>first:
            first=num
    return first

def get_largest_1(test_list):
    return max(test_list)

def get_largest_2(test_list):
    test_list.sort()
    return test_list[-1]

def get_largest_3(test_list):
    return sorted(test_list)[-1]

test_list=[5, 1, 16, 8, 2, 12, 3]
# test_list=[5]
# test_list=[]
# test_list=[5, 7, 8, 8]
print(get_largest(test_list))
