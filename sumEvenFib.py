import sys

sum = 0

#for i in range(1,(int(sys.argv[1]))) :
def fibSequence(limit):
		evens_sum = 0
		i = 1
		last = 0
		current = 0
		while (i <= limit):
				if (i % 2 == 0):
						print(i)
						evens_sum += i
				current = i
				i += last
				last = current
		print("sum: ",evens_sum)
		return 0

fibSequence(int(sys.argv[1]))
#for i in range(int(sys.argv[1])) :
#	if (i > 0 and i % 2 == 0) :
#				sum+=i
#				print(i)
#print(sum)
quit()
