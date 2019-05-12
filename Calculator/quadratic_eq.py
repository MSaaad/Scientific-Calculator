def Quadratic():
    while True:
        first_num=int(input('Enter value of co-efficient with ^2:'))
        sec_num=int(input('Enter value of co-efficient with ^1:'))
        constant=int(input('Enter value of constant:'))
        print(first_num,str('x^2'),'+',sec_num,str('x'),'+',constant)
        d=((sec_num**2)-(4*first_num*constant))**0.5
        x1=(-sec_num-d)/(2*first_num)
        x2=(-sec_num+d)/(2*first_num)
        print('The roots of the following Equation are.......')
        print('The First root is',x1)
        print('The second root is',x2)
