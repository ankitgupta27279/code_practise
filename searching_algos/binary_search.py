def binary_search_rec(arr, target, start, end):
    if start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            return binary_search_rec(arr, target, mid+1, end)
        else:
            return binary_search_rec(arr, target, start, mid-1)
    else:
        return -1

def binary_search_iter(arr, target):
    low=0
    high=len(arr)-1
    while low<=high and target>=arr[low] and target<=arr[high]:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<=target:
            low=mid+1
        else:
            high=mid-1
    return -1


if __name__=="__main__":
    arr=[19, 2, 11, 6, 1, 12, 8, 3]
    target=8
    # print(binary_search_rec(sorted(arr), target, 0, len(arr)-1))
    print(binary_search_iter(sorted(arr), target))