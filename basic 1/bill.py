#WAP to generate electricity bill
''' accept number of units consumed
if units>0 and units<=100 cost is 10rs/unit
if units>100 and units<=200 cost is 15rs/unit
if units>200 and units<=300 cost is 20rs/unit
otherwise 25rs/unit
'''
unit=int(input("enter number of unit:"))
cost=0
if(unit<=100):
    cost=10*unit;
elif(unit<=200):
    cost=(10*100)+15*(unit-100);
elif(unit<=300):
    cost=(10*100)+(15*100)+25*(unit-200);
else:
    cost=(10*100)+(15*100)+(25*100)+25*(unit-300);

print("cost=",cost)
    
