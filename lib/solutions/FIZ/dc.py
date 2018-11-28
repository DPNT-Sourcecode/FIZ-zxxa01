def dc(number):
    nstr=str(number)
    for i, d in enumerate(nstr):
	print('i=',i,"d=",d)
	if i == 0:
	    prev_d = d
	if prev_d == d:
	   isSame = True
	   prev_d = d
	   print('i=',i,"d=",d, 'prev_d=',' prev_d')
	else:
	   return False

	return isSame


#test function

print dc(654)
print dc(333)
