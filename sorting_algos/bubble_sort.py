import time
from typing import List

def get_sorted_bubble_sort(test_list: List) -> List:
    for i in range(len(test_list)):
        swapped=False
        for j in range(0, len(test_list)-i-1):
            if test_list[j]>test_list[j+1]:
                test_list[j], test_list[j+1] = test_list[j+1], test_list[j]
                swapped=True
        if not swapped:
            break
    return test_list



if __name__=="__main__":
    start_time=time.time()
    # test_list=[5,6,1,3]
    test_list=[64, 34, 25, 12, 22, 11, 90]
    print(get_sorted_bubble_sort(test_list))
    end_time=time.time()
    print(f"time consumed--->{(end_time-start_time)*1000} ms")
