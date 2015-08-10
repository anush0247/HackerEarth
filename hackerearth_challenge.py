def NthFib(n):
	if(n <= 1):
		return 0
	elif(n == 2 or n == 3):
		return 1
	else :
		return NthFib(n-1) + NthFib(n-2)

def fibnoci(n,m):

	if(n <= 1):
		return 0
	elif (n == 2):
		return 1
	elif (n == 3):
		return 2
	else :
		return  NthFib(n,m)+fibnoci(n-1,m)

def FibSumRange(l,r):
	sum  = 0
	for i in range(l+1,r+1):
		sum += NthFib(i)
	return sum

n = raw_input()
n = int(n,10)
arr = list()
for i in range(n):
	t = raw_input().split()
	#print (fibnoci() - fibnoci(int(t[0],10))) 
	print FibSumRange(int(t[0],10),int(t[1],10))