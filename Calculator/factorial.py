def factorial():
    while True:
        factorial=1
        x=int(input('Enter Number'))
        for i in range(1,x+1):
            factorial=factorial*i
        print(factorial)
        if x==0:
            print('The factorial of zero is 1')
        elif x<0:
            print('please enter positive number')
    
