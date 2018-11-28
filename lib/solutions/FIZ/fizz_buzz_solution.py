# noinspection PyUnusedLocal
def fizz_buzz(number):

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
    	    return 'fizz'
	elif isDivFive(number) or containsFive(number):
    	    return 'buzz'
	else:
     	    return number

        if number==0:
	    return number
   	 
#test function 
for i in range (-4,35):
	print(i,fizz_buzz(i))

