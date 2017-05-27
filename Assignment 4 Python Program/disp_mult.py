def multipleofseven(num):
	if(num%7)==0:
		return True
	else:
		return False
		
def multipleofthirteen(num):
	if(num%13)==0:
		return True
	else:
		return False


print("A program in python")

for counter in range(30,300):
    anynum=multipleofseven(counter)
    othernum=multipleofthirteen(counter)
    if (anynum==True and othernum==True):
    	print "a-z"
    elif anynum==True:
    	print "abc"
    elif othernum==True:
    	print "xyz"
    else:
    	print counter
    
