import math
n = int(raw_input('enter an integer'))

sum = 0
for i in range(2,n):
	for p in range(2,int(math.sqrt(i))+1):
		if i % p == 0:
			break
	else:
		sum += i 
			
		
print sum