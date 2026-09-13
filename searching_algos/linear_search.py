def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1


if __name__=="__main__":
    arr = [2, 3, 4, 10, 40]
    # target=10
    target=11
    print(linear_search(arr, target))
