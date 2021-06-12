#import PROBAprogramm

def mply(a=[], b=[]):
	c=[]
	for i in range(len(a)):
		c.append([])
		for j in range(len(b[0])):
			c[i].append(0)
			for i1 in range(len(a[0])):
				ci = a[i][i1] * b[i1][j]
				c[i][j] += ci
	return c

def gauss(a = []):
	b = [0 for i in range(len(a))]
	for i in range(len(a)):
		for k in range(i+1, len(a)):
			z = a[k][i]/a[i][i]
			for j in range(i, len(a)+1):
				a[k][j] -= z * a[i][j]
	b[-1] = a[-1][-2]/a[-1][-1]
	i = len(a)-1
	while i >=0:
		b[i] = a[i][len(a[0])-1]
		for j in range(i+1, len(a[0])-1):
			b[i] -= a[i][j]*b[j]
		b[i] /= a[i][i]
		b[i] = round(b[i], 2)
		i -= 1
	return b

def trans(a = []):
	b = [[0 for j in range(len(a))] for i in range(len(a[0]))]
	for i in range(len(a[0])):
		for j in range(len(a)):
			b[i][j] = a[j][i]
	return b