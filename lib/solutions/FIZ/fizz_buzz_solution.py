# noinspection PyUnusedLocal
def fizz_buzz(number):

	def isDeluxe(number):
            if number < 10:
                return False
    	    nstr=str(number)
	    prev=False
    	    for i in range(len(nstr)):
        	#print('i=',i,"nstr[i]=",nstr[i])
        	if i == 0:
            	    prev = nstr[i]
        	elif prev == nstr[i]:
           	   isSame = True
           	   prev = nstr[i]
           	   #print('i=',i,"d=",nstr[i], 'prev_d=',' prev_d')
        	else:
           	   return False

            return isSame



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
     	    op= str(number)

	if (isDivFive(number) or containsFive(number)) and (isDivThree(number) or containsThree(number)) :
    	    op= 'fizz buzz'

        if (isDeluxe(number)):
	    if op==str(number):
	       op="deluxe"
	    else:
	       op = op + " deluxe"

        if number==0:
	    op= str(number)

	return op 
   	 
#test function 
#for i in range (-4,35):
#	print(i,fizz_buzz(i))

print (10, fizz_buzz(10))
print (12, fizz_buzz(12))
print (11, fizz_buzz(11))
print (1111, fizz_buzz(1111))
print (15, fizz_buzz(15))
print (33, fizz_buzz(33))
print (22, fizz_buzz(22))
print (30, fizz_buzz(30))
print (465, fizz_buzz(465))
print (444, fizz_buzz(465))
print (555, fizz_buzz(555))
print (500, fizz_buzz(500))






