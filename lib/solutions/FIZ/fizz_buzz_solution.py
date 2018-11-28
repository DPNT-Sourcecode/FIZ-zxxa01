# noinspection PyUnusedLocal
def fizz_buzz(number):
     fcheck=divmod(number,3)
     bcheck=divmod(number,5)
     if (fcheck[1]==0) and (bcheck[1]==0):
 	op="fizz buzz"
     elif (fcheck[1]==0) and (bcheck[1]!=0):
	op="fizz"
     elif (fcheck[1])!=0 and (bcheck[1]==0):
	op="buzz"
     elif (number=0):
	op==number

     else:
	     op=number
     return  op 

#test function 
for i in range (-4,16):
	print(i,fizz_buzz(i))
