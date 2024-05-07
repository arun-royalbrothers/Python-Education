#reverse string using recurssion
def reverse_str(str, n, result=""):
    if n<0:
        return result
    letter = str[n]
    result+=letter
    return reverse_str(str, n-1, result)

a = "Arun Arunisto"
print(reverse_str(a, len(a)-1))

#reverse an integer using recurrsion
def reverse_int(num, result=0):
    if num == 0:
        return result
    digit = num%10
    result = result*10+digit
    num//=10
    return reverse_int(num, result)
print(reverse_int(123))

# 06.05.2024
#reverse string 
def reverse_str(str, result=""):
    if str == "":
        return result
    result += str[-1]
    return reverse_str(str[:-1], result)

#palindrome
def palindrome_str(str):
    if str == "":
        return True
    if str[0] == str[-1]:
        return palindrome_str(str[1:-1])
    return False

#recursion with int
#palindrome
def palindrome_str(str):
    if str == "":
        return True
    if str[0] == str[-1]:
        return palindrome_str(str[1:-1])
    return False

#sum of natural numbers
def sum_numbers(num, result=0):
    if num == 0:
        return result
    result+=num
    return sum_numbers(num-1, result)

#sum of natural numbers - FCC 
def sum_of_num(num):
    if num <= 1:
        return num
    return num+sum_of_num(num-1)

## 07.05.2024
#binary search
def binary_search(li, start, end, target):
    if start > end:
        return False
    mid = (start+end)//2
    if li[mid] == target:
        return True
    if target < li[mid]:
        return binary_search(li, start, mid-1, target)
    else:
        return binary_search(li, mid+1, end, target)

#fibonacci series
def fib_series(n):
    if n <= 1:
        return n
    return fib_series(n-1) + fib_series(n-2)

#merge sort
def merge_sort(li):
    if len(li) < 2:
        return li
    mid = len(li)//2
    left_arr = li[0:mid]
    right_arr = li[mid:len(li)]
    return merge(merge_sort(left_arr), merge_sort(right_arr))

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
    
