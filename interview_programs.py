"""
    *
   * *
  * * *
 * * * *
* * * * * 
Q1: Pattern program 
"""
#solution 1
def pyramidPattern(n):
    for i in range(n): #<- rows
        #loop for the space
        for j in range(1, n-i): #<- columns
            print(" ", end="")
        #loop for the star with a space
        for s in range(i+1): #<- columns
            print("*", end=" ")
        #for splitting columns
        print()

pyramidPattern(5)
"""
* * * * *
 * * * *
  * * *
   * *
    *
Q2: Reverse pattern
"""
#solution2
def reversePyramid(n):
    for i in range(n): #<- rows
        for j in range(i): #<- space columns
            print(" ", end="")
        for s in range(n-i): #<- star columns with one space
            print("*", end=" ")
        print() #<- splitting columns

reversePyramid(5)

"""
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
Q3: Card pattern
"""
#solution3
def cardPattern(n):
    """
    code for the first half pattern
    **********
    ****  ****
    ***    ***
    **      **
    *        *
    """
    for i in range(n):
        for j in range(n-i):
            print("*", end="")
        for s in range(i):
            print(" ", end=" ")
        for p in range(n-i):
            print("*", end="")
        print()
    """
    Again code for another half
    *        *
    **      **
    ***    ***
    ****  ****
    **********
    """
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        for s in range(1, n-i):
            print(" ",end=" ")
        for p in range(i+1):
            print("*", end="")
        print()
cardPattern(5)
"""
    0
   1 2
  3 4 5
 6 7 8 9
Q4: numeric pattern
"""
#solution4
def numericPattern(n):
    no = 0
    for i in range(n):
        for j in range(1, n-i):
            print(" ", end="")
        for s in range(i+1):
            print(no, end=" ")
            no+=1
        print()
numericPattern(4)
"""
str = "arunisto"
rev = "otsinura"
Q5: Reverse a string using for loop
"""
#solution5
def reverse(str):
    s = "".join(
        list(
            str[i] for i in range(len(str)-1, -1, -1)
            )
        )
    return s
print(reverse("arunisto"))
"""
li = ["arun", "arunisto", "python"]
reverse = ["python", "arunisto", "arunisto"]
Q6: Reversing a list using for loop
"""
#solution6
def reverseList(list):
    new_li = [list[i] for i in range(len(list)-1, -1, -1)]
    return new_li
print(reverseList(["arun", "arunisto", "python"]))
"""
Function for converting integer to binary
"""
def binaryNumber(num):
    bin_li = []
    half = num
    while half > 0:
        temp = half
        half//=2
        bin_li.insert(0, str(temp%2))
    return "".join(bin_li)
"""
Fibonacci number function
"""
def fibonacciNum(num):
    fib_li = []
    num1 = 0
    num2 = 1
    for i in range(num):
        fib_li.append(num1)
        temp = num1
        num1 = num2
        num2+=temp
    print(*fib_li)
"""
Primenumber or not
"""
def isPrime(num):
    if num < 2:
        return False
    if num > 2:
        for i in range(2, (num//2)+1):
            if num%i == 0:
                return False
    return True
"""
Function for converting binary to integer
"""
def binary2Integer(binary):
    bin_li = []
    for i in range(len(str(binary))-1, -1, -1):
        bin_li.append(str(binary)[i])
    result = 0
    for i in range(len(bin_li)):
        result+=(int(bin_li[i])*(2**i))
    return result
"""
HackerRank Day 11: 2D arrays
"""
li = [[1, 1, 1, 0, 0, 0],
      [0, 1, 0, 0, 0, 0],
      [1, 1, 1, 0, 0, 0],
      [0, 0, 2, 4, 4, 0],
      [0, 0, 0, 2, 0, 0],
      [0, 0, 1, 2, 4, 0]]
#print(li)
sum = 0
tarr = []
for l in range(0, 4):
    for k in range(0, 4):
        for i in range(l,l+3):
            #print(f"i:{i}", end="")
            for j in range(k,k+3):
                if i == l+1 and (j == k or j == k+2):
                    #print("i",i,"j",j,"l",l,"k",k)
                    continue
                else:
                    sum+=li[i][j]
        tarr.append(sum)
        sum = 0
print(max(tarr))
"""
Bubble sort
"""
def bubbleSort(arr):
   for i in range(len(arr)):
      for j in range(len(arr)-1):
         if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
   return arr
"""
prime number with less time complexity
"""
def prime_number(number):
   if number <= 1:
      return False
   if number == 2:
      return True
   if number%2 == 0:
      return False
   for i in range(3, int(number**0.5)+1, 2):
      if number %i == 0:
         return False
   return True
"""
Text Wrap
"""
import textwrap

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
width = 4

print(textwrap.wrap(string, width))
#output:
"""
['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST', 'UVWX', 'YZ']
"""

print(textwrap.fill(string, width))
#output:
"""
ABCD
EFGH
IJKL
MNOP
QRST
UVWX
YZ
"""
"""
Method overloading using multipledispatch module
"""
from multipledispatch import dispatch

class sampleClass:
    @dispatch(int, int)
    def add(self, a, b):
        return a+b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a+b+c

obj = sampleClass()
print(obj.add(23, 45)) #68
print(obj.add(23, 45, 66)) #134
"""
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
"""
n = 7
m = 21
for i in range(n//2):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))
print('WELCOME'.center(m, '-'))
for i in reversed(range(n//2)):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))
"""
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
"""
width = len(bin(17)[2:])
for i in range(1, 17+1):
    dec_i = str(i)
    oct_i = oct(i)[2:]
    hex_i = hex(i)[2:].upper()
    bin_i = bin(i)[2:]
    print(dec_i.rjust(width), oct_i.rjust(width), hex_i.rjust(width), bin_i.rjust(width))
"""
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
letters = "abcdefghijklmnopqrstuvwxyz"
def print_rangoli(size):
    lines = []
    for row in range(size):
        print_ = "-".join(letters[row:size])
        lines.append(print_[::-1]+print_[1:])
    #print(lines)
    width = len(lines[0])
    for row in range(size-1, 0, -1):
        print(lines[row].center(width, "-"))
    for row in range(size):
        print(lines[row].center(width, "-"))
"""
hackerrank minion solution
"""
def minion_game(string):
    n = len(string)
    comb = ((n)*(n+1))/2
    #print(comb)
    count_k = sum([len(string[i:]) for i in range(len(string)) if string[i] in "aeiou"])
    count_s = comb - count_k
    if count_s == count_k:
        print("Draw")
    elif count_s > count_k:
        print("Stuart",int(count_s))
    else:
        print("Kevin", int(count_k))

minion_game("banana")
"""
1
121
12321
1234321
123454321
"""
n = int(input())
for i in range(1, n+1):
   print(((10**i-1)//9)**2)
"""
PixDynamics @decorator function
"""
def odd_dec(func):
    def wrapper(a, b):
        if (a%2!=0 and b%2!=0):
            return a+b
        else:
            return func(a, b)
    return wrapper

@odd_dec
def sum(a, b):
    return a+b

print(sum(3, 5))
"""
li = [1, 2, 3, 4, 5]
result = [3, 2, 1]
"""
li = [1, 2, 3, 4, 5]
print(li[2::-1])
"""
Leet code : 383. Ransom Note
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            pos = ransomNote[i]
            matchIndex = magazine.find(pos)
            if matchIndex == -1:
                return False
            magazine = magazine[:matchIndex]+magazine[matchIndex+1:]
        return True
"""
Leet code : 13. Roman to Integer
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
        "I":1, "V":5, "X":10, "L":50,
        "C":100, "D":500, "M":1000}
        ans = 0
        for i in range(0, len(s)-1):
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                ans -= roman_dict[s[i]]
            else:
                ans += roman_dict[s[i]]
        return ans+roman_dict[s[-1]]

"""
0(log n) Binary Search
"""
def binary_search(array, start, end, target):
    mid = (start+end)//2
    if start > end:
        return False
    if array[mid] == target:
        return True
    if array[mid] > target:
        return binary_search(array, start, mid-1, target)
    else:
        return binary_search(array, mid+1, end, target)

li = [1, 2, 3, 4, 5, 6, 7, 8]
target = 10
start = 0
end = len(li)-1
print(binary_search(li, start, end, target))

"""
O(n log n) Merge Sort
"""
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    #finding mid point
    mid = len(arr)//2
    #creating two arrays
    left_arr = arr[0:mid]
    right_arr = arr[mid:len(arr)]
    #calling merge function it acts like recursion
    return merge(mergeSort(left_arr), mergeSort(right_arr))

#merge function
def merge(left_arr, right_arr):
    #creating new array to save the sort merged list
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

li = [35, 43, 12, 27, 5, 90, 17, 8]
print(mergeSort(li))

"""
O(2^n) - Fibnoacci Series
"""
def fib_series(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_series(n-1)+fib_series(n-2)

n = 10
for i in range(n):
    print(fib_series(i), end=" ")

"""
O(n!) - factorial
"""
def fac(n):
    li = []
    if n == 0:
        
        return
    for i in range(n):
        fac(n-1)

fac(3)
"""
O(n) - Factorial
"""
def fac(n):
   if n==1:
      return 1
   else:
      temp = fac(n-1)
      temp*=n
      return temp
      
"""
O(n) - Permutattion
"""
def permutattion(str, packet=""):
   if len(str) == 0:
      print(packet)
   else:
      for i in range(len(str)):
         letter = str[i]
         front = str[0:i]
         back = str[i+1:]
         together = front+back
         permutation(together, letter+packet)
"""
GFG - GreedyFox - Time Complexity (0(n))
"""
def greedyFox(arr):
    max_s = arr[0]
    cur_s = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            cur_s+=arr[i]
            if cur_s > max_s:
                max_s = cur_s
        else:
            cur_s = arr[i]
    return max_s

print(greedyFox([2, 1, 4, 7, 3, 6]))
"""
LeetCode - Climbing Stairs
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        steps = [1, 1]+[0]*(n-1)
        for i in range(2, n+1):
            steps[i] = steps[i-1]+steps[i-2]
        return steps[n]
"""
LeetCode - Remove Duplicates from sorted linkedlist
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
"""
Pascal's Triangle Leetcode
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result
        result.append([1])
        if numRows == 1:
            return result
        for i in range(1, numRows):
            prev_li = result[i-1]
            in_li = []
            in_li.append(1)
            for j in range(i-1):
                in_li.append(prev_li[j]+prev_li[j+1])
            in_li.append(1)
            result.append(in_li)
        return result
"""
Longest Common Prefix
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        strs.sort()
        first_word = strs[0]
        last_word = strs[-1]
        for i in range(len(first_word)):
            if first_word[i] == last_word[i]:
                result+=first_word[i]
            else:
                break
        return result
"""
Insertion Sort
"""
def insertionSort(li):
   for i in range(1, len(li)):
      key = li[i]
      j = i-1
      while j>=0 and li[j] > key:
         li[j+1] = li[j]
         j-=1
      li[j+1] = key
   return li
"""
LeetCode 20. Valid Parenthesis
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        li = []
        for i in range(len(s)):
            if len(li) == 0 and s[i] in (")", "]", "}"):
                return False
            if s[i] == "(":
                li.append(")")
            elif s[i] == "[":
                li.append("]")
            elif s[i] == "{":
                li.append("}")
            elif s[i] == li[-1]:
                li.pop()
            else:
                return False
        if len(li) == 0:
            return True
        else:
           return False
"""
121. Best time to buy and sell stock
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_pri = prices[0]
        max_pro = 0
        curr_pro = 0
        for i in range(1, len(prices)):
            if curr_pri < prices[i]:
                curr_pro = prices[i] - curr_pri
                if curr_pro > max_pro:
                    max_pro = curr_pro
            else:
                curr_pri = prices[i]
        return max_pro
"""
169. Majority Element - Solving using Voting Algorithm
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        votes = 1
        for i in range(1, len(nums)):
            if nums[i] == majority:
                votes+=1
            else:
                if votes == 0:
                    majority = nums[i]
                    votes = 0
                else:
                    votes-=1
        return majority
"""
Reverse an Integer
"""
#Reversing an intger
def reverse_int(num):
    result = 0
    while num > 0:
        digit = num%10
        result = result*10+digit
        num//=10
    return result



