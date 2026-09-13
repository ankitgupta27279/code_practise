import time
from typing import List

def get_sorted_selection_sort(test_list: List) -> List:
    for i in range(len(test_list)-1):
        min_index=i
        for j in range(i+1, len(test_list)):
            if test_list[min_index]>test_list[j]:
                min_index=j
        test_list[i], test_list[min_index] = test_list[min_index], test_list[i]
    return test_list



if __name__=="__main__":
    start_time=time.time()
    # test_list=[5,6,1,3]
    test_list=[64, 34, 25, 12, 22, 11, 90]
    print(get_sorted_selection_sort(test_list))
    end_time=time.time()
    print(f"time consumed--->{(end_time-start_time)*1000} ms")

