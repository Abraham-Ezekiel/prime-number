#!/usr/bin/env python3
"""a =[3,45,6,7,3,4,3,5,7,7,8,8,2]
name = 'bughacker'
for _ in name:
	print('good morning')
"""

#range:  is use to generate number

'''
for i in range(1, 11):
	if i%2==0:
		print(i)
'''

for j in range(1, 101):

	if j>1 and (j==2 or j==3 or j==5 or j==7 or (j % 2 != 0 and j%3 !=0 and j%5 !=0 and j%7 !=0)):
		print(j)
'''
import math
for j in range(1, 101):
    if j > 1:  # 0 and 1 are not prime numbers
        is_prime = True
        for i in range(2, int(math.sqrt(j)) + 1):
            if j % i == 0:
                is_prime = False
                break
        if is_prime:
            print(j)
'''
