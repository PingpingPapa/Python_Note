def palindrome(s):
    ss = list(s)
    for i in range(len(ss)):
        if ss[-i-1] != ss[i]:
            return False
    return True

print(palindrome("tomato"))
print(palindrome("ldlddldl"))
print(palindrome("dad"))
print(palindrome("tomasdfato"))
