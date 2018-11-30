"""
Project Euler 
Problem 19 - Counting Sundays
"""
import datetime 

count = 0
for y in range(1901,2001):
	for m in range(1,13):
		if datetime.date(y, m, 1).isoweekday() == 6:
			count += 1

print(count)
