# noinspection PyUnusedLocal
def fizz_buzz(number):

	def isDeluxe(n):
	    if n > 10: 
 	str.find(str(number),'3')!= -1:
	        return  True 	  
	    else:
                 return False

	def containsThree(n):
	    if str.find(str(number),'3')!= -1:
	        return  True 	  
	    else:
                 return False

	def containsFive(n):
	    if str.find(str(number),'5')!= -1:
	        return  True 	  
	    else:
                 return False

	def isDivThree(n):
	    if (n%3) == 0:
	        return  True 	  
	    else:
                 return False

	def isDivFive(n):
	    if (n%5) == 0:
	        return  True 	  
	    else:
                 return False

	if isDivThree(number) or containsThree(number):
    	    op= 'fizz'
	elif isDivFive(number) or containsFive(number):
    	    op= 'buzz'
	else:
     	    op= number

	if (isDivFive(number) or containsFive(number)) and (isDivThree(number) or containsThree(number)) :
    	    op= 'fizz buzz'

        if number==0:
	    op= number

	return op 
   	 
#test function 
#for i in range (-4,35):
#	print(i,fizz_buzz(i))

print (15, fizz_buzz(15))
print (30, fizz_buzz(30))
print (465, fizz_buzz(465))

