import sys

sum = 0;

#for i in range(1,(int(sys.argv[1]))) :
for i in range(int(sys.argv[1])) :
		if (i > 0 and i % 2 == 0) :
				sum+=i
				print(i)
print(sum)
quit()
