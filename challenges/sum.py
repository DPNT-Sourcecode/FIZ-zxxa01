def sum (int1, int2):
    if type(int1) not in [int] or type(int2) not in [int]:
        raise TypeError("The arguments must be integer")
    return int1+int2

#test function

for i in range(1,100,1):
    print(i, sum(i,1))

#test function - type error
print(i, sum('one',1))

