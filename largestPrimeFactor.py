#find largest prime factor of 600851475143.

import sys
import math

#create a list of factors for n
def getLargestPrimeFactor(num):
		int_sqrt = round(math.sqrt(num))
		primeFactors = list()
		for i in range(int_sqrt,0,-1):
				if (num%i == 0):
						highFactor = int(num/i)
						if (isPrime(highFactor)):
								return highFactor
						if (isPrime(i)):
								primeFactors.append(i)
		#if we found primes on the lower half return largest
		return primeFactors[0]

#create a list of factors for n
#def getFactors(num):
#		f = [1, num]
#		int_sqrt = round(math.sqrt(num))
#		for i in range(int_sqrt,1,-1):
#				if (num%i == 0):
#						f.append(i)
#						f.append(int(num/i))
#
#		return sorted(f)

#largest prime factor
#def findLargestPrime(factor_list):
#		for i in range(len(factor_list)-1,-1,-1):
#				if isPrime(factor_list[i]):
#						print(factor_list[i])
#						return
#		print("No prime factors for ")
#		print(factor_list)
#		return

def isPrime(num):
		primeBool = False
		#rule out the quick ones
		if (num%2 == 0 or num%5 == 0 or num%3 == 0 or num%7 == 0):
				return primeBool

		#case where number has a regular integer as its sqrt
		theSqrt = math.sqrt(num)
		#if (num%round(math.sqrt(num)) == 0):
		if (theSqrt == round(theSqrt)):
				return primeBool
		
		for i in range(round(theSqrt)-1,2,-1):
				if (num%i == 0):
					return primeBool
	    
		primeBool = True
		return primeBool

n = int(sys.argv[1])
#return largest prime factor
print(getLargestPrimeFactor(n))


quit()
