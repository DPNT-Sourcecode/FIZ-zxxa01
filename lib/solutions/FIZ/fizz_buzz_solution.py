# noinspection PyUnusedLocal
def fizz_buzz(number):
	def isDivThree(n):
	    if (n%3) == 0:
		  
     fcheck=divmod(number,3)
     bcheck=divmod(number,5)
     if (fcheck[1]==0) and (bcheck[1]==0):
 	op="fizz buzz"
     elif (fcheck[1]==0) and (bcheck[1]!=0):
	op="fizz"
     elif (fcheck[1])!=0 and (bcheck[1]==0):
	op="buzz"
     else:
	   op=number
     if (number==0):
	op=number
     return  op 

#test function 
#for i in range (-4,16):
#	print(i,fizz_buzz(i))

