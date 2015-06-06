#one lined comments
'''
Doc Strings
'''


first_name = "Kermit"
last_name = "De Frog"

#response = raw_input ("Enter your name   -    ")
#print response

birth_year = 1988
current_year = 2015
age = current_year - birth_year
print "You are " + str(age -1) + " years old."

budget = 99

if budget > 100:
	brand = "nike"
	print "Yay! we can buy cool " + brand + " shoes! "
elif budget > 50:
	print "We can atleast get some generic sneakers."
else:
	pass
