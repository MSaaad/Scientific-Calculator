
def factorial(a):
    if a==0:
        return 1
    else:
        return a*factorial(a-1)
    
def ncr(n,r):
        ncr = factorial(n)/factorial(r)*(factorial(n-r))
        print(ncr)
    
def npr(n,r):
        npr = factorial(n)/factorial(n-r)
        print(npr)
    

