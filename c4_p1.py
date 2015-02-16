def fib(num):
	if num == 1 or num == 2:
		return 1
	else:
		return fib(num - 1) + fib(num - 2)
n = 100		
current = 0
i = 1
sum = 0
while current <= n:
	if current % 2 == 0:
		sum = sum + current
	current = fib(i)
	i += 1


print sum		
		
		