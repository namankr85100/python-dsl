# function to calculate the factorial 
def fact (n):
	if n == 0:
		return 1 
	return n * fact (n - 1)

# Main code 
num = 4

# Factorial
print "Factorial of {0} is: {1} ".format (num, fact(num))