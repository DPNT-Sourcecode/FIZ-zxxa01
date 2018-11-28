def sum (int1, int2):
#    if type(int1) not in [int] or type(int2) not in [int]:
        #raise TypeError("The arguments must be integer")
    #if (int1 < 0) or (int1 > 100) or (int2 < 0) or (int2 > 100):
        #raise valueError("The arguments must be in range 0-100")
    return int1+int2

#test function

for i in range(0,100,1):
    print(i, sum(i,1))

#print(i, sum( -1,0))

#test function - type error
#print(i, sum('one',1))


