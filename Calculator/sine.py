
def sin():
    
    while True:
        x=int(input('Enter the angle:'))
        x=x*0.01745329252
        sin=x-(x**3/6)+(x**5/120)-(x**7/5040)
        print(sin)


