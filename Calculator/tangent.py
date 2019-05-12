
def tan():
    while True:
        x=int(input('Enter the angle:'))
        x=x*0.01745329252
        Sin=x-(x**3/6)+(x**5/120)-(x**7/5040)
        Cos=1-(x**2/2)+(x**4/24)-(x**6/720)
        tan=Sin/Cos
        print(tan)

