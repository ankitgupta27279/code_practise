import time
from typing import List

def get_sorted_insertion_sort(test_list: List) -> List:
    if len(test_list)<=1:
        return
    for i in range(1, len(test_list)):
        key=test_list[i]
        j=i-1
        while j>=0 and key<test_list[j]:
            test_list[j+1]=test_list[j]
            j-=1
            print(f"test_list 1--->{test_list}")
        test_list[j+1]=key
        print(f"test_list 2--->{test_list}")
    return test_list


if __name__=="__main__":
    start_time=time.time()
    # test_list=[5,6,1,3]
    # test_list=[64, 34, 25, 12, 22, 11, 90]
    test_list=[12, 11, 13, 5, -1]
    print(get_sorted_insertion_sort(test_list))
    end_time=time.time()
    print(f"time consumed--->{(end_time-start_time)*1000} ms")