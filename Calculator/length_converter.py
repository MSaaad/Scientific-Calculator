def length_converter():
    while True:
        x=int(input('Enter Length to be converted  :'))
        y=input('Enter the unit of the length specied  :')
        z=input('Enter the unit in which length is to converted  :')
        if y=='m' and z=='cm':
            print(x*100,z)
        elif y=='cm' and z=='m':
            print(x/100,z)
        elif y=='m' and z=='km':
            print(x*1000,z)
        elif y=='km' and z=='m':
            print(x/1000,z)
        elif y=='cm' and z=='km':
            print(x*100000,z)
        elif y=='km' and z=='cm':
            print(x/100000,z)
        else:
            print('Please enter length measuring matrices!')
        
        
