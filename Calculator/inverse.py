
print('give your angle in degree like if 1/2 rad write 30')
print("""sin30=1/2       cos30=3^0.5/2       tan30=3^0.5/3
sin45=2^0.5/2   cos45=2^0.5/2       tan45=1
sin60=3^0.5/2   cos60=1/2           tan60=3^0.5
sin90=1         cos90=0             tan90=infinity""")
h=input('enter your choice \npress X for arcsin \npress Y for arccos \npress Z for arctan')
if h=='X':
    a=int(input("value?"))
    c=(a/180)*3.142
    print(c,'rad')
    d=input('if you want your answer in degree press A')
    if d=='A':
        print((c*180)/3.142,'degree')

if h=='Y':
    a=int(input("value?"))
    c=(a/180)*3.142
    print(c,'rad')
    d=input('if you want your answer in degree press A')
    if d=='A':
        print((c*180)/3.142)
    
if h=='Z':
    a=int(input("value?"))
    if a==90:
        print('infinty')
    else:
        c=(a/180)*3.142
        print(c)
        d=input('if you want your answer in degree press A')
    if d=='A':
        print((c*180)/3.142,'degree')

