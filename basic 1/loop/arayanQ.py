L = []

Num = int( input( " Enter number of element: " ) )

for I in range(0,Num):
    Element = int(input( " Enter element {}: ".format( I + 1 ) ))
    L.append(Element)
    
print( " Data in the list: ", L )
    
for N in L:
    if N % 2 == 0:
        print( N, " is even number. " )
    else:
        print( N, " is odd number. " )