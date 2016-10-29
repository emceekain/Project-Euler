def IntegerSum(n):
	sum = int(n*(n+1)/2)
	return sum

#Makes IntegerSum usable as  script
if __name__=="__main__":
	import sys
	IntegerSum(int(sys.argv[1]))
