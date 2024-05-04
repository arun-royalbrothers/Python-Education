#reverse string using recurssion
def reverse_str(str, n, result=""):
    if n<0:
        return result
    letter = str[n]
    result+=letter
    return reverse_str(str, n-1, result)

a = "Arun Arunisto"
print(reverse_str(a, len(a)-1))
