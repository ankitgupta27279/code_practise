def get_second_smallest(nums: List) -> int:
    if len(nums)<1:
        print("empty list")
        return None
    first=second=float('inf')
    for num in nums:
        if num<first:
            second=first
            first=num
        elif first<num and num<second:
            second=num
    return second if second!=float('inf') else None

test_list=[5, 1, 16, 8, 2, 12, 3]
# test_list=[5]
# test_list=[]
# test_list=[5, 7, 7, 8]
# test_list=[10, 4, 3, 50, 23, 90]
# test_list=[5, 7]
print(get_second_smallest(test_list))
