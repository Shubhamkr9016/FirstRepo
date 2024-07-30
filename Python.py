# finding the gcd of two numbers.

n = int(input("enter the number: "))  # taking input from the user
m = int(input("enter the number: "))  # taking input from the user
def gcd(n,m):              # defining a function gcd
    fm = []                # creating an empty list
    fn = []
    for i in range(1,n+1):          # using for loop to find the factors of the number
        if n%i==0:                # checking the condition  if n is divisible by i
            fn.append(i)          # appending the factors of n to the list
    for i in range(1,m+1):        # using for loop to find the factors of the number
        if m%i==0:                  # checking the condition  if m is divisible by i
            fm.append(i)           # appending the factors of m to the list
    cf = []                         # creating an empty list
    for i in fn:                    # using for loop to find the common factors of n and m
        if i in fm:                  # checking the condition if i is in fm
            cf.append(i)             # appending the common factors to the list
    return cf[-1]                    # returning the last element of the list
print("The gcd of",n,"and",m,"is",gcd(n,m))    # printing the gcd of the numbers

