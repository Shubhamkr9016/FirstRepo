# finding the gcd of two numbers.

n = int(input("enter the number: "))  
m = int(input("enter the number: "))
def gcd(n,m):
    fm = []
    fn = []
    for i in range(1,n+1): 
        if n%i==0:
            fn.append(i)
    for i in range(1,m+1):
        if m%i==0:
            fm.append(i)
    cf = []
    for i in fn:
        if i in fm:
            cf.append(i)
    return cf[-1]
print("The gcd of",n," and",m, "is", gcd(n,m))

