from __future__ import print_function
import math, sys
from decimal import *
python2 = sys.version_info[0] == 2
if python2:
	input = raw_input
n = int(input("How many digits?: "))

def factorial(n):
	"""
	Return the Factorial of a number using recursion
	Parameters:
	n -- Number to get factorial of
	"""
	if not n:
		return 1
	return n*factorial(n-1)
def getIteratedValue(k):
	"""
	Return the Iterations as given in the Chudnovsky Algorithm.
	k iterations gives k-1 decimal places.. Since we need k decimal places
	make iterations equal to k+1

	Parameters:
	k  -- Number of Decimal Digits to get
	"""
	k = k+1
	getcontext().prec = k
	sum=0
	for k in range(k):
		first = factorial(6*k)*(13591409+545140134*k)
		down = factorial(3*k)*(factorial(k))**3*(640320**(3*k))
		sum += first/down
	return Decimal(sum)


iter = getIteratedValue(n)
up = 426880*math.sqrt(10005)
pi = Decimal(up)/iter
print (pi)
