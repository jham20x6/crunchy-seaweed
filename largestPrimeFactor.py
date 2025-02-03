#find largest prime factor of 600851475143.

import sys
import math

#create a list of factors for n
def getLargestPrimeFactor(dividend):
	int_sqrt = round(math.sqrt(dividend))
	highestPrimeDivisor = 1
	for divisor in range(int_sqrt,0,-1):
		if (dividend%divisor == 0):
			quotient = int(dividend/divisor)
			if (isPrime(quotient)):
				return quotient
			if (isPrime(divisor)):
				if (highestPrimeDivisor == 1):
					highestPrimeDivisor = divisor
	#if we found primes on the lower half return largest
	return highestPrimeDivisor
			

def isPrime(num):
	primeBool = False
	if (num > 2):
		for i in range(2,round(math.sqrt(num))):
			if (num % i == 0):
				return primeBool
	
	primeBool = True
	return primeBool

n = int(sys.argv[1])
#return largest prime factor
print(getLargestPrimeFactor(n))

quit()
