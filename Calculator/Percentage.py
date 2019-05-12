
def percentage():
    while True:
        c=input('Criteria:')
        a=int(input('Obtained:'))
        b=int(input('Total:'))
        print('You have obtained',a,'out of',b,c)
        print('The calculated percentage is.....')
        ans=(a/b)*100
        print('=',ans,'%',sep='')
#percentage()
