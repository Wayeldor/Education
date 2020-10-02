h=input('enter pay hours:')
r=input('enter rate')
try:
    hour=float(h)
    rate=float(r)
except:
    print('please enter a numeric value')
    quit()
    
if rate>40:
    pay=(40*rate)+((hours-40)*rate*1.5)
else:
    pay=rate*hour
print(pay)
