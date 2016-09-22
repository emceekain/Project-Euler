def IntegerSum(n):
	sum = int(n*(n+1)/2)
	return sum

#Makes fib usable as  script
if __name__=="__main__":
	import sys
	IntegerSum(int(sys.argv[1]))
