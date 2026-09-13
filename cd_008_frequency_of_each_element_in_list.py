def get_frequeny_of_each_element(nums: List) -> List:
    test_dict={}
    for num in nums:
        if num in test_dict.keys():
            test_dict[num]+=1
        else:
            test_dict[num]=1
    return test_dict


test_list=[7, 1, 7, 3, 5, 8, 3, 2, 1, 9, 9, 2, 9]
print(get_frequeny_of_each_element(test_list))
