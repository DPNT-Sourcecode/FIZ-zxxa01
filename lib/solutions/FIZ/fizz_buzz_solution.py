# noinspection PyUnusedLocal
def fizz_buzz(number):

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

	if isDivThree(number):
    	    return 'fizz'
	elif isDivFive(number):
    	    return 'buzz'
	else:
     	    return number
   	 
#test function 
for i in range (-4,16):
	print(i,fizz_buzz(i))



