### find kth largest and kth smallest element in array

import heapq

def get_kth_largest_kth_smallest_1(test_list, k):
    test_list.sort()
    kth_largest=test_list[-k]
    kth_smallest=test_list[k-1]
    return kth_largest, kth_smallest

def get_kth_largest_kth_smallest_2(test_list, k):
    kth_smallest=heapq.nsmallest(k, test_list)[-1]
    kth_largest=heapq.nlargest(k, test_list)[-1]
    return kth_largest, kth_smallest

def get_kth_largest_kth_smallest_3(test_list, k):
    test_list=sorted(test_list)
    kth_largest=test_list[-k]
    kth_smallest=test_list[k-1]
    return kth_largest, kth_smallest


test_list=[12, 3, 5, 7, 19, 26]
k=2
print(get_kth_largest_kth_smallest_3(test_list, k))
