import sys

sum = 0;

#for i in range(1,(int(sys.argv[1]))) :
def fibSequence(previous,current,limit):
		if (current > limit):
				return
		next_digit = previous + current
		if (next_digit % 2 == 0): 
			if (next_digit <= limit):
				sum+=fibSequence(current, next_digit, limit)
			else:
				return (sum)


fibSequence(1,1,int(sys.argv[1]))
#for i in range(int(sys.argv[1])) :
#	if (i > 0 and i % 2 == 0) :
#				sum+=i
#				print(i)
#print(sum)
quit()
