def get_missing_num_in_sequence(nums: List) -> List:
    start=nums[0]
    missing_num=None
    for num in nums[1:]:
        if start+1==num:
            start=num
        else:
            missing_num=start+1
            break
    return missing_num


# test_list=[1, 2, 4, 5]
test_list=[23, 24, 26, 27]
print(get_missing_num_in_sequence(test_list))