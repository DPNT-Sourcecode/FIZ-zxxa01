# noinspection PyUnusedLocal
def fizz_buzz(number):
     fcheck=divmod(number,3)
     bcheck=divmod(number,5)
     if (fcheck[1]==0) and (bcheck[1]==0):
 	op="fizz buzz"
	elif (fcheck[1]==0) and (bcheck[1]!=0) :
	    op="fizz"
	    elif (fcheck[1]!=0 and bcheck[1]==0):
	        op="buzz"
        else op=number
    return = op 

#test function 

print fizz_buzz(10)


