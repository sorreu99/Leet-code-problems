x = 33

# sol1


def isPalindrome1(x):
    if x >= 0:
        rev = int("".join(str(x)[::-1]))

        if x == rev:

            return True
        else:
            return False
    else:
        
        return False


print(isPalindrome1(x))


# sol2
def isPalindrome(x):
    if x > 0:
        p = str(x)
        a = ""
        nums = []
        for item in reversed(p):
            a += item
        a = int(a)
        if a == x:
            return True
        else:
            return False
    else:
        return False


print(isPalindrome(x))
