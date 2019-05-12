def log():
    log0=0
    log1=0
    log2=0.3010
    log3=0.4771
    log4=0.6020
    log5=0.6989
    log6=0.7781
    log7=0.8450
    log8=0.9030
    log9=0.9542
    log10=1
    print('If your value is e.g 459 so please write like this 4.59 ')
    x=float(input('value'))
    y=int(input('value after decimal'))
    z=int(input('decimal places'))
    if x==1:
        print(log1)
    elif x>1 and x<2:
        a=log2-log1
        b=(a*(10**-z))
        c=round(b*y,4)
        d=log1+c
        print(d)
        h=int(input('do u want your asnwer in whole no. form e.g 4.5 in 45 if yes press 0'))
        if h==0:
            print(d+z)
        else:
            exit
    elif x==2:
        print(log2)
    elif x>2 and x<3:
        a=log3-log2
        b=(a*(10**-z))
        c=round(b*y,4)
        d=log2+c
        print(d)
        h=int(input('do u want your asnwer in whole no. form e.g 4.5 in 45 if yes press 0'))
        if h==0:
            print(d+z)
        else:
            exit
    elif x==3:
        print(log3)
    elif x>3 and x<4:
        a=log4-log3
        b=(a*(10**-z))
        c=round(b*y,4)
        d=log3+c
        print(d)
        h=int(input('do u want your asnwer in whole no. form e.g 4.5 in 45 if yes press 0'))
        if h==0:
            print(d+z)
        else:
            exit
    elif x==4:
        print(log4)
    elif x>4 and x<5:
        a=log5-log4
        b=(a*(10**-z))
        c=round(b*y,4)
        d=log4+c
        print(d)
        h=int(input('do u want your asnwer in whole no. form e.g 4.5 in 45 if yes press 0'))
        if h==0:
            print(d+z)
        else:
            exit

    elif x==5:
        print(log5)
    elif x>5 and x<6:
        a=log6-log5
        b=(a*(10**-z))
        c=round(b*y,4)
        d=log5+c
        print(d)
        h=int(input('do u want your value in whole no. form e.g 4.5 in 45 if yes press 0'))
        if h==0:
            print(d+z)
        else:
            exit
    elif x==6:
        print(log6)
    elif x>6 and x<7:
        a=log7-log6
        b=(a*(10**-z))
        c=round(b*y,4)
        d=log6+c
        print(d)
        h=int(input('do u want your value in whole no. form e.g 4.5 in 45 if yes press 0'))
        if h==0:
            print(d+z)
        else:
            exit
    elif x==7:
        print(log7)
    elif x>7 and x<8:
        a=log8-log7
        b=(a*(10**-z))
        c=round(b*y,4)
        d=log7+c
        print(d)
        h=int(input('do u want your value in whole no. form e.g 4.5 in 45 if yes press 0:'))
        if h==0:
            print(d+z)
        else:
            exit
    elif x==8:
        print(log8)
    elif x>8 and x<9:
        a=log6-log5
        b=(a*(10**-z))
        c=round(b*y,4)
        d=log8+c
        print(d)
        h=int(input('do u want your value in whole no. form e.g 4.5 in 45 if yes press 0:'))
        if h==0:
            print(d+z)
        else:
            exit
    elif x==9:
        print(log5)
    elif x>9 and x<10:
        a=log9-log10
        b=(a*(10**-z))
        c=round(b*y,4)
        d=log9+c
        print(d)
        h=int(input('do u want your value in whole no. form e.g 4.5 in 45 if yes press 0'))
        if h==0:
            print(d+z)
        else:
            exit
log()
