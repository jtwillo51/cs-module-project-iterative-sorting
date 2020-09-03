from iterative_sorting import bubble_sort
def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    first = 0
    last = len(arr) -1
    found = False
    while(first<= last and not found):
        mid = (first + last) //2
        if arr[mid] == target:
            found = True
            
        else:
            if target < arr[mid]:
                last = mid -1
            else:
                first = mid +1
    if found == True:
        return mid
    else:
        return -1  # not found 

