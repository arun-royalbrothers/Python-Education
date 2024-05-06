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

