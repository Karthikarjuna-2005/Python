units=int(input())
if units<200:
    uc=1.20
elif units>=200 and units<400:
    uc=1.50
elif units>=400 and units<600:
    uc=1.80
else:
    uc=2.00

bill=units*uc
if bill>=400:
    totalbill=bill+(bill*0.15)
    print('{:.2f}'.format(totalbill))
else:
    totalbill=bill+100
    print('{:.2f}'.format(totalbill))
          
