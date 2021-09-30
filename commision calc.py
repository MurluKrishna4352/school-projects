#Progm to clculte the commission on the bsis of sles mde tken s the input
'''
sales                 commision
>20000               3000 or 20% sles
>=15000 & <=20000   2500   or 15% sales
>=10000 & <15000    2000   or 10% sales
<10000               nil    0
'''
sales = float(input("Enter your saled amount:    "))

if (sales>20000):
    print("commision: ", sales*(20/100))
if (sales>=15000 and sales<=20000):
    print("commision: ", sales*(15/100))
if (sales>=10000 and sales<15000):
    print("commision: ", sales*(10/100))
if (sales<10000):
    print("no pain no gain")

