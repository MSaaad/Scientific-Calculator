def ln():
    num=int(input('Enter Value of ln:'))
    a=(num)**(1/32768)
    b=a-1
    c=(b/0.000070271)

    x=(2.71828188)**(1/32768)
    y=x-1
    z=(y/0.000070271)

    ln=c/z
    print(ln)
