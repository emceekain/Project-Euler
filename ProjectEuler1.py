## Project Euler #1
## If we list all the natural numbers below 10 that are multiples of 3 or 5,
## we get 3, 5, 6 and 9. The sum of these multiples is 23.
## Find the sum of all the multiples of 3 or 5 below 1000.

from IntegerSum import IntegerSum

def SumofMultiplesof3and5(n):
	mod3 = n%3
	mod5 = n%5
	mod15= n%15
	if mod3 == 0:
		threes = 3*IntegerSum(n/3-1)
	else:
		threes = 3*IntegerSum((n-mod3)/3)
	if mod5 == 0:
		fives = 5*IntegerSum(n/5-1)
	else:
		fives = 5*IntegerSum((n-mod5)/5)
	if mod15 ==0:
		fifteens = 15*IntegerSum(n/15-1)
	else:
		fifteens = 15*IntegerSum((n-mod15)/15)
	total = threes + fives - fifteens
	print (total)

#Makes usable as  script
if __name__=="__main__":
	import sys
	SumofMultiplesof3and5(int(sys.argv[1]))