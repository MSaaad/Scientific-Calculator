def base_conv(num,base):
    string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if num<base:
        return string[num]
    else:
        return base_conv(num//base,base) + string[num%base]
    
