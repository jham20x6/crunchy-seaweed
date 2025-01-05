import sys

sum = 0;

#for i in range(1,(int(sys.argv[1]))) :
def fibSequence(previous,current,limit):
		fib_sum = previous + current
		print(fib_sum)
		if (fib_sum <= limit):
				print(fib_sum, end=", ")
				fibSequence(current, fib_sum, limit)
		else:
				print("fib_sum", fib_sum)
				return


fibSequence(1,1,int(sys.argv[1]))
#for i in range(int(sys.argv[1])) :
#	if (i > 0 and i % 2 == 0) :
#				sum+=i
#				print(i)
#print(sum)
quit()
