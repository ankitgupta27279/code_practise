### 10. Rotate a list by k positions.

def left_rotate_list_by_position(nums: List, k: int) -> List:
    k%=len(nums)
    return nums[k:]+nums[:k]


def right_rotate_list_by_position(nums: List, k: int) -> List:
    k%=len(nums)
    return nums[-k:]+nums[:-k]


def get_rotated_list(nums: List, direction: str, index: int):
    final_data=[]
    index%=len(nums)
    if direction=="right":
        final_data=nums[-index:]+nums[:-index]
    elif direction=="left":
        final_data=nums[index:]+nums[:index]
    return final_data


test_list=[1, 2, 3, 4, 5, 6, 7]
k=9
print(left_rotate_list_by_position(test_list, k))
print(right_rotate_list_by_position(test_list, k))
print(get_rotated_list(nums, "right", 2))
print(get_rotated_list(nums, "left", 12))
