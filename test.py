
def isPalindrome( x) :
    if x >=0:
        rev = int("".join(str(x)[::-1]))
        if  x==rev:
             return True
        else:

             return False
    elif x <0:
        return False

y=print(isPalindrome(121))