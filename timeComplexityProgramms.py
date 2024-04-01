#O(1) - Constant
def mid_idx(arr):
    mid = len(arr)//2
    return mid
print(mid_idx([1, 2, 3, 4, 5, 6]))
#O(n) - Linear Search
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(linearSearch([1, 2, 3, 4, 5, 6], 5))
#O(n^2) - Bubble Sort Algorithm
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubbleSort([34, 12, 23, 55, 99, 101, 6]))
#O(log n) - Binary Search Algorithm
def binarySearch(arr, start, end, target):
    if start > end:
        return -1
    mid = (start+end)//2
    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return binarySearch(arr, start, mid-1, target)
    else:
        return binarySearch(arr, mid+1, end, target)
li = [1, 2, 3, 4, 5, 6, 7, 8]
print(binarySearch(li, 0, len(li)-1, 7))
#O(n log n) - Merge Sort Algorithm
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left_arr = arr[0:mid]
    right_arr = arr[mid:len(arr)]
    return merge(mergeSort(left_arr), mergeSort(right_arr))
def merge(left_arr, right_arr):
    result = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] < right_arr[right_idx]:
            result.append(left_arr[left_idx])
            left_idx+=1
        else:
            result.append(right_arr[right_idx])
            right_idx+=1
    return result+left_arr[left_idx:]+right_arr[right_idx:]
li = [34, 12, 23, 55, 99, 101, 6]
print(mergeSort(li))
#O(2^n) - Fibnoacci Series
def fib_series(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_series(n-1) + fib_series(n-2)

for i in range(5):
    print(fib_series(i), end=" ")
#O(n!) - Factorial
def factorial(n):
    if n == 0:
        print("*****")
        return
    for i in range(n):
        factorial(n-1)
factorial(3)

    
