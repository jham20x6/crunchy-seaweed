#find largest prime factor of 600851475143.

import sys
import math

#create a list of factors for n
def getFactors(num):
		f = [1]
		int_sqrt = round(math.sqrt(num))
		for i in range(2,int_sqrt):
				if (num%i == 0):
						f.append(i)

		if (num%int_sqrt == 0):
				f.append(int_sqrt)

		for item in reversed(f):
				f.append(int(num/item))

		return(f)

#largest prime factor
def findLargestPrime(factor_list):
		for i in range(len(factor_list)-1,-1,-1):
				if isPrime(factor_list[i]):
						print(factor_list[i])
						return
		print("No prime factors for ")
		print(factor_list)
		return

def isPrime(num):
		#cut down on time, check if it's divisible by 2 or 5 right away.
		if (num != 2 and num!=5 and num!=3 and num!=7):
				if (num%2 == 0 or num%5 == 0 or num%3 == 0 or num%7 == 0):
						return False
		#create a list of factors for n
		factors = getFactors(num)
		#evaluate the list for primeness ( only 2 factors )
		if (len(factors) == 2):
				#primeStatus = ' is prime!'
				primeBool = True
		else:
				#primeStatus = ' is NOT prime =('
				primeBool = False
	    
		#print(factors)
		#print(factors[len(factors)-1], primeStatus)
		return primeBool

n = int(sys.argv[1])
isPrime(n)
findLargestPrime(getFactors(n))

#return largest prime factor
quit()
