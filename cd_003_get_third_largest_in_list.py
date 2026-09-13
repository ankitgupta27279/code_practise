def get_third_largest(nums: List) -> int:
    if len(nums)<1:
        print("empty list")
        return None
    first=second=third=float('-inf')
    for num in nums:
        if num>first:
            third=second
            second=first
            first=num
        elif first>num and num>second:
            third=second
            second=num
        elif second>num and num>third:
            third=num
    return third if third!=float('-inf') else None

    
# test_list=[5, 1, 16, 8, 2, 12, 3]
# test_list=[5]
# test_list=[]
# test_list=[5, 7, 5, 8]
test_list=[10, 4, 3, 50, 23, 90]
# test_list=[5, 7]
print(get_third_largest(test_list))
