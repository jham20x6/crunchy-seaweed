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
lpf = 0

#create a list of factors for n
n = int(sys.argv[1])
factors = list()
factors = getFactors(n)

print(factors)
if (len(factors) == 2):
		print(n,' is prime!')
else:
		print(n,' is NOT prime =(')

#evaluate the list for prime-ness
#return largest prime factor

#for i in range(int(sys.argv[1])) :
#		if (i % 5 == 0 or i % 3 == 0) :
#				sum+=i
#print(sum)
quit()
