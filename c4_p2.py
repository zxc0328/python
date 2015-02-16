g_year = int(raw_input('year:'))
g_month = int(raw_input('month:')) 
count=0
year=1800
month=[31,28,31,30,31,30,31,31,30,31,30,31]
day= 1 + 365 %7
while year <= g_year:
    if (year%4==0 and year%100!=0) or year%400==0:
        month[1]=29
    else:
        month[1]=28
	if year == g_year:	
		for mon in range(12): 
			day += month[mon]
			day = day%7
	else:
		for mon in range(g_month): 
			day += month[mon]
			day = day%7
			
    year += 1
print (day + month[g_month-1]-1)%7


		
		
		