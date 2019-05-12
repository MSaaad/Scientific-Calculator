def radian(x):
    print((x/180)*(22/7))
def degree(x):
    print((x*180)/3.142)
print('\tAngle Conversion')
print('1.Covert into radian','\n2.Convert into Degree')
choice='integer'
while choice:
    choice=int(input('Enter Your Choice'))
    if choice==1:
        x=float(input('enter your angle in degree'))
        radian(x)
    elif choice==2:
        x=float(input('enter your angle in radian'))
        degree(x)
    else:
        print('select your choice correclty')
    
