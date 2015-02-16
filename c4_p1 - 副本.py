def fib(num):
	if num == 1 or num == 2:
		return 1
	else:
		return fib(num - 1) + fib(num - 2)
		
n = int(raw_input('put an integer'))
current = 0
sum = 0

while current <= n:
	if fib(current) % 2 == 0:
		sum += fib(current)
		current += 1
	else:
		current += 1
	
	
		
		

print sum




		
		
		