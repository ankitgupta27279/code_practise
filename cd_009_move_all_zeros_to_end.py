### 9. Move all zeros to the end while maintaining the order of other elements.

def get_updated_list(nums: List) -> List:
    zeros_list=[]
    i=0
    while i<len(nums):
        if nums[i]==0:
            zeros_list.append(nums.pop(i))
        else:
            i+=1
        print(f"nums--->{nums}")
    nums.extend(zeros_list)
    return nums

def get_new_list(nums):
    zeros_list=[]
    non_zeros_list=[]
    for num in nums:
        if num==0:
            zeros_list.append(num)
        else:
            non_zeros_list.append(num)
    non_zeros_list.extend(zeros_list)
    return non_zeros_list    


test_list=[2, 0, 1, 4, 5, 0, 6, 2, 0, 1]
result_list=get_updated_list(test_list)
print(result_list)
if len(test_list)==len(result_list):
    print(f"length of both lists are same")
