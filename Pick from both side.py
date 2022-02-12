a=[5,-2,3,1,2]
b=3

def solve(a,b):
    arr=a[:b]
    val=sum(a[:b])
    imax=val
    for x in range(0,b):
        rem=arr.pop()
        addd=a.pop()
        val=val-rem+addd
        imax=max(val,imax)
    return imax

print(solve(a,b))