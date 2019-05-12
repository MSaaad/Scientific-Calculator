def calculation(a):
    while True:
        print('''
Now operate the number with the following operation!

1.Addition            2.Subtraction        3.Multiplication
4.Division            5.Percentage         6.Reciprocal
7.Cos                 8.Sin                9.Tan    ''' )

        operation=int(input('\nEnter the operation you want to perform:'))

        sec_num=int(input('Enter second number:'))
        
        if operation==1:
            ans=a+sec_num
            print('addition of',a,'and',sec_num,'is',ans)
        elif operation==2:
            ans=a-sec_num
            print('subtraction of',a,'and',sec_num,'is',ans)
        elif operation==3:
            ans=a*sec_num
            print('multiplication of',a,'and',sec_num,'is',ans)
        elif operation==4:
            ans=a/sec_num
            print('division of',a,'and',sec_num,'is',ans)
        elif operation==5:
            ans=(a/sec_num)*100
            print('=',ans,'%',sep='')

        elif operation==6:
            ans=sec_num/a
            print('reciprocal of',sec_num,'and',a,'is',ans)
        elif operation==7:
            a=a*0.01745329252
            ans=1-(a**2/2)+(a**4/24)
            print('The angle is',ans)
        elif operation==8:
            a=a*0.01745329252
            ans=a-(a**3/6)+(a**5/120)
            print('The angle is',ans)
        elif operation==9:
            a=a*0.01745329252
            Sin=a-(a**3/6)+(a**5/120)
            Cos=1-(a**2/2)+(a**4/24)
            ans=Sin/Cos
            print('The angle is',ans)
        
        a=ans
first_num=int(input('Enter first number:'))
calculation(first_num)
                               
