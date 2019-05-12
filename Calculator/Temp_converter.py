def temperature_converter():

    while True:
        x=int(input('Enter Temperature  :'))
        y=input('Enter the scale of the temperature specied  :')
        z=input('Enter the scale in which temperature is to converted  :')
        if y=='C' and z=='F':
            print((x*1.8)+32,z)
        elif y=='F' and z=='C':
            print((x-32)*0.5556,z)
        elif y=='C' and z=='K':
            print(x+273,z)
        elif y=='K' and z=='C':
            print(x-273,z)
        elif y=='K' and z=='F':
            print((x*1.8)-459.67,z)
        elif y=='F' and z=='K':
            print((x+459.67)*0.5556,z)
        
