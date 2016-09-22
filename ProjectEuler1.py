## Project Euler #1
from IntegerSum import IntegerSum

def SumofMultiplesof3and5(n):
	if n % 3 == 0:
		threes = 3*IntegerSum(n/3-1)
	else:
		threes = 3*IntegerSum((n-n%3)/3)
	if n % 5 == 0:
		fives = 5*IntegerSum(n/5-1)
	else:
		fives = 5*IntegerSum((n-n%5)/5)
	total = threes + fives
	print (total)

#Makes usable as  script
if __name__=="__main__":
	import sys
	SumofMultiplesof3and5(int(sys.argv[1]))