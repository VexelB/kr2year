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

def printMatrix(a=[]):
  for i in range(len(a)):
    for j in range(len(a[0])):
      print('%10f' % a[i][j], end=" ")
    print()

def changeMatrix(k, M = []):
  for j in range(0, len(M) + 1):
    (M[k][j],  M[len(M) - k - 1][j]) = (M[len(M) - k -1][j], M[k][j])

def factorV1(a=[]):

  L = [[0 for j in range(len(a))] for i in range(len(a))]
  R = [[0 for j in range(len(a))] for i in range(len(a))]

  n = len(L) - 1

  for i in range(len(L)):
    L[i][0] = a[i][0]

  R[0][0] = 1

  for j in range(1, n + 1):
    R[0][j] = a[0][j]/(L[0][0])

  for j in range(1, n + 1):
    R[j][j] = 1
    for i in range(j, n + 1):
      S = 0
      for k in range(0, j):
        S += L[i][k]*R[k][j]
      L[i][j]  = a[i][j] - S
    i = j
    for t in range(j + 1, n + 1):
      S = 0
      for k in range(0, i):
        S += L[i][k]*R[k][t]
      R[i][t] = (a[i][t] - S)/L[i][i]

  L1 = []
  R1 = []

  for i in range(len(L)):
    L1.append([])
    for j in range(len(L[0])):
      L1[i].append(round(L[i][j], 5))
  for i in range(len(R)):
    R1.append([])
    for j in range(len(R[0])):
      R1[i].append(round(R[i][j], 5))

  Z = [0 for i in range(len(a))]
  X = [0 for i in range(len(a))]

  Z[0] = a[0][-1]/L[0][0]
  for i in range(1, n + 1):
    S = 0
    for k in range(0, i):
      S += L[i][k]*Z[k]
    Z[i] = (a[i][-1] - S)/L[i][i]

  X[n] = Z[n]/(R[n][n])
  for i in range(n - 1, -1, -1):
    S = 0
    for k in range(i + 1, n + 1):
      S += R[i][k]*X[k]
    X[i] = (Z[i] - S)/R[i][i]

  X1 = []
  for i in range(len(X)):
    X1.append([])
    X1[i].append(round(X[i], 5))

  return ( L1, R1, X1 )

def factorV2(a=[]):
  L = [[0 for j in range(len(a))] for i in range(len(a))]
  R = [[0 for j in range(len(a))] for i in range(len(a))]
  n = len(L) - 1
  for i in range(len(L)):
    L[i][n] = a[i][n]

  R[n][n] = 1

  for j in range(0, n):
    R[n][j] = a[n][j]/(L[n][n])

  for j in range(n - 1, -1, -1):
    R[j][j] = 1
    for i in range(j, -1, -1):
      S = 0
      for k in range(j + 1, n + 1):
        S += L[i][k]*R[k][j]
      L[i][j] = a[i][j] - S


    i = j
    for t in range(i - 1, -1, -1):
      S = 0
      for k in range(i + 1, n + 1):
        S += L[i][k]*R[k][t]
      R[i][t] = (a[i][t] - S)/L[i][i]

  L1 = []
  R1 = []

  for i in range(len(L)):
	  L1.append([])
	  for j in range(len(L[0])):
		  L1[i].append(round(L[i][j], 5))
  for i in range(len(R)):
	  R1.append([])
	  for j in range(len(R[0])):
		  R1[i].append(round(R[i][j], 5))
  Z = [0 for i in range(len(a))]
  X = [0 for i in range(len(a))]

  Z[n] = a[n][-1]/L[n][n]
  for i in range(n - 1, -1, -1):
    S = 0
    for k in range(i + 1, n + 1):
      S += L[i][k]*Z[k]
    Z[i] = (a[i][-1] - S)/L[i][i]

  X[0] = Z[0]/(R[0][0])
  for i in range(1, n + 1):
    S = 0
    for k in range(0, i):
      S += R[i][k]*X[k]
    X[i] = (Z[i] - S)/R[i][i]

  X1 = []
  for i in range(len(X)):
    X1.append([])
    X1[i].append(round(X[i], 5))

  return ( L1, R1, X1 )


def factorV3(a=[]):
  L = [[0 for j in range(len(a))] for i in range(len(a))]
  R = [[0 for j in range(len(a))] for i in range(len(a))]
  n = len(L) - 1
  for i in range(len(L)):
    L[i][0] = a[i][n]

  R[0][n] = 1

  for j in range(0, n):
    R[0][j] = a[0][j]/(L[0][0])

  for j in range(1, n + 1):
    R[j][n - j] = 1
    for i in range(j, n + 1):
      S = 0
      for k in range(0, j):
        S += L[i][k]*R[k][n - j]
      L[i][j] = a[i][n - j] - S

    i = j
    for t in range(n - i - 1, -1, -1):
      S = 0
      for k in range(0, i):
        S += L[i][k]*R[k][t]
      R[i][t] = (a[i][t] - S)/L[i][i]

  L1 = []
  R1 = []

  for i in range(len(L)):
	  L1.append([])
	  for j in range(len(L[0])):
		  L1[i].append(round(L[i][j], 5))
  for i in range(len(R)):
	  R1.append([])
	  for j in range(len(R[0])):
		  R1[i].append(round(R[i][j], 5))
  Z = [0 for i in range(len(a))]
  X = [0 for i in range(len(a))]

  Z[0] = a[0][-1]/L[0][0]
  for i in range(0, n + 1):
    S = 0
    for k in range(0, i):
      S += L[i][k]*Z[k]
    Z[i] = (a[i][-1] - S)/L[i][i]

  X[0] = Z[-1]/R[n][0]
  for i in range(1, n + 1):
    p = n - i
    S = 0
    for k in range(0, i):
      S += R[p][k]*X[k]
    X[i] = (Z[p] - S)/R[p][i]
    X[i] = round(X[i], 5)

  X1 = []
  for i in range(len(X)):
    X1.append([])
    X1[i].append(round(X[i], 5))

  return ( L1, R1, X1 )

def factorV4(a=[]):
  L = [[0 for j in range(len(a))] for i in range(len(a))]
  R = [[0 for j in range(len(a))] for i in range(len(a))]
  n = len(L) - 1
  for i in range(len(L)):
    L[i][0] = a[i][0]

  R[0][0] = 1

  for j in range(1, n + 1):
    R[0][j] = a[n][j]/(L[n][0])

  for j in range(n - 1, -1, -1):
    R[n - j][n - j] = 1
    for i in range(j, -1, -1):
      S = 0
      for k in range(0,  n - j + 1):
        S += L[i][k]*R[k][n - j]
      L[i][n - j] = a[i][n - j] - S

    i = j
    for t in range(n - i + 1, n + 1):
      S = 0
      for k in range(0, n - i + 1):
        S += L[i][k]*R[k][t]
      R[n - i][t] = (a[i][t] - S)/L[i][n - i]

  L1 = []
  R1 = []

  for i in range(len(L)):
	  L1.append([])
	  for j in range(len(L[0])):
		  L1[i].append(round(L[i][j], 5))
  for i in range(len(R)):
	  R1.append([])
	  for j in range(len(R[0])):
		  R1[i].append(round(R[i][j], 5))
  Z = [0 for i in range(len(a))]
  X = [0 for i in range(len(a))]

  Z[0] = a[n][-1]/L[n][0]
  for i in range(1, n + 1):
    p = n - i
    S = 0
    for k in range(0, i):
      S += L[p][k]*Z[k]
    Z[i] = (a[p][-1] - S)/L[p][i]

  X[n] = Z[-1]/R[n][n]
  for i in range(n - 1,-1, -1):
    S = 0
    for k in range(i + 1, n + 1):
      S += R[i][k]*X[k]
    X[i] = (Z[i] - S)/R[i][i]
    X[i] = round(X[i], 5)

  X1 = []
  for i in range(len(X)):
    X1.append([])
    X1[i].append(round(X[i], 5))

  return ( L1, R1, X1 )

def factorV5(a=[]):
  L = [[0 for j in range(len(a))] for i in range(len(a))]
  R = [[0 for j in range(len(a))] for i in range(len(a))]
  n = len(L) - 1
  for i in range(len(L)):
    L[i][n] = a[i][n]

  R[n][n] = 1

  for j in range(0, n):
    R[n][j] = a[0][j]/(L[0][n])

  for j in range(1, n + 1):
    R[n - j][n - j] = 1
    for i in range(j, n + 1):
      S = 0
      for k in range(n - j + 1, n + 1):
        S += L[i][k]*R[k][n - j]
      L[i][n - j] = a[i][n - j] - S

    i = j
    for t in range(n - i - 1, -1, -1):# for t in range(i + 1, n + 1):
      S = 0
      for k in range(t  + 1, n + 1):
        S += L[i][k]*R[k][t]
      R[n - i][t] = (a[i][t] - S)/L[i][n - i]

  L1 = []
  R1 = []

  for i in range(len(L)):
	  L1.append([])
	  for j in range(len(L[0])):
		  L1[i].append(round(L[i][j], 5))
  for i in range(len(R)):
	  R1.append([])
	  for j in range(len(R[0])):
		  R1[i].append(round(R[i][j], 5))
  Z = [0 for i in range(len(a))]
  X = [0 for i in range(len(a))]

  Z[n] = a[0][-1]/L[0][n]
  for i in range(n - 1, -1, -1):
    p = n - i
    S = 0
    for k in range(i + 1, n + 1):
      S += L[p][k]*Z[k]
    Z[i] = (a[p][-1] - S)/L[p][i]

  X[0] = Z[0]/(R[0][0])
  for i in range(1, n + 1):
    S = 0
    for k in range(0, i):
      S += R[i][k]*X[k]
    X[i] = (Z[i] - S)/R[i][i]
    X[i] = round(X[i], 5)

  X1 = []
  for i in range(len(X)):
    X1.append([])
    X1[i].append(round(X[i], 5))

  return ( L1, R1, X1 )

def factorV6(a=[]):
  L = [[0 for j in range(len(a))] for i in range(len(a))]
  R = [[0 for j in range(len(a))] for i in range(len(a))]
  n = len(L) - 1
  for i in range(len(L)):
    L[i][n] = a[i][0]

  R[n][0] = 1

  for j in range(1, n + 1):
    R[n][j] = a[n][j]/(L[n][n])

  for j in range(n - 1, -1, -1):
    R[j][n - j] = 1
    for i in range(j, -1, -1):
      S = 0
      for k in range(i+1, n + 1):
        S += L[i][k]*R[k][n - j]
      L[i][j] = a[i][n - j] - S
    i = j
    for t in range(j - 1, -1,-1):
      S = 0
      for k in range(i + 1, n + 1):
        S += L[i][k]*R[k][n-t]
      R[i][n-t] = (a[i][n-t] - S)/L[i][i]

  L1 = []
  R1 = []

  for i in range(len(L)):
	  L1.append([])
	  for j in range(len(L[0])):
		  L1[i].append(round(L[i][j], 5))
  for i in range(len(R)):
	  R1.append([])
	  for j in range(len(R[0])):
		  R1[i].append(round(R[i][j], 5))
  Z = [0 for i in range(len(a))]
  X = [0 for i in range(len(a))]

  Z[n] = a[n][-1]/L[n][n]
  for i in range(n - 1, -1, -1):
    S = 0
    for k in range(i + 1, n + 1):
      S += L[i][k]*Z[k]
    Z[i] = (a[i][-1] - S)/L[i][i]

  X[n] = Z[0]/(R[0][n])
  for i in range(n - 1, -1, -1):
    p = n - i
    S = 0
    for k in range(i + 1, n + 1):
      S += R[p][k]*X[k]
    X[i] = (Z[p] - S)/R[p][i]
    X[i] = round(X[i], 5)

  X1 = []
  for i in range(len(X)):
    X1.append([])
    X1[i].append(round(X[i], 5))

  return ( L1, R1, X1 )


def factorV7(a=[]):
  L = [[0 for j in range(len(a))] for i in range(len(a))]
  R = [[0 for j in range(len(a))] for i in range(len(a))]
  n = len(L) - 1
  for i in range(len(L)):
    L[i][0] = a[i][n]

  R[0][n] = 1

  for j in range(n-1, -1, -1):
    R[0][j] = a[n][j]/(L[n][0])

  for j in range(n - 1, -1, -1):
    R[n - j][j] = 1
    for i in range(j, -1, -1):
      S = 0
      for k in range(0, n - j + 1):
        S += L[i][k]*R[k][j]
      L[i][n - j] = a[i][j] - S

    i = j
    for t in range(i - 1, -1,-1):
      S = 0
      for k in range(0, n - i + 1):
        S += L[i][k]*R[k][t]
      R[n - i][t] = (a[i][t] - S)/L[i][n - i]

  L1 = []
  R1 = []

  for i in range(len(L)):
	  L1.append([])
	  for j in range(len(L[0])):
		  L1[i].append(round(L[i][j], 5))
  for i in range(len(R)):
	  R1.append([])
	  for j in range(len(R[0])):
		  R1[i].append(round(R[i][j], 5))

  Z = [0 for i in range(len(a))]
  X = [0 for i in range(len(a))]

  Z[0] = a[n][-1]/L[n][0]
  for i in range(1, n + 1):
    p = n - i
    S = 0
    for k in range(0, i):
      S += L[p][k]*Z[k]
    Z[i] = (a[p][-1] - S)/L[p][i]

  X[0] = Z[-1]/R[n][0]
  for i in range(1, n + 1):
    p = n - i
    S = 0
    for k in range(0, i):
      S += R[p][k]*X[k]
    X[i] = (Z[p] - S)/R[p][i]
    X[i] = round(X[i], 5)

  X1 = []
  for i in range(len(X)):
    X1.append([])
    X1[i].append(round(X[i], 5))

  return ( L1, R1, X1 )

def factorV8(a=[]):
  L = [[0 for j in range(len(a))] for i in range(len(a))]
  R = [[0 for j in range(len(a))] for i in range(len(a))]
  n = len(L) - 1
  for i in range(len(L)):
    L[i][n] = a[i][0]

  R[n][0] = 1

  for j in range(1, n + 1):
    R[n][j] = a[0][j]/(L[0][n])

  for j in range(1, n + 1):
    R[n - j][j] = 1
    for i in range(j, n + 1):
      S = 0
      for k in range(n - j + 1, n + 1):
        S += L[i][k]*R[k][j]
      L[i][n - j] = a[i][j] - S

    i = j
    for t in range(i + 1, n + 1):# for t in range(i + 1, n + 1):
      S = 0
      for k in range(n - t + 1, n + 1):
        S += L[i][k]*R[k][t]
      R[n - i][t] = (a[i][t] - S)/L[i][n - i]

  L1 = []
  R1 = []

  for i in range(len(L)):
	  L1.append([])
	  for j in range(len(L[0])):
		  L1[i].append(round(L[i][j], 5))
  for i in range(len(R)):
	  R1.append([])
	  for j in range(len(R[0])):
		  R1[i].append(round(R[i][j], 5))
  Z = [0 for i in range(len(a))]
  X = [0 for i in range(len(a))]

  Z[n] = a[0][-1]/L[0][n]
  for i in range(n - 1, -1, -1):
    p = n - i
    S = 0
    for k in range(i + 1, n + 1):
      S += L[p][k]*Z[k]
    Z[i] = (a[p][-1] - S)/L[p][i]

  X[n] = Z[0]/(R[0][n])
  for i in range(n - 1, -1, -1):
    p = n - i
    S = 0
    for k in range(i + 1, n + 1):
      S += R[p][k]*X[k]
    X[i] = (Z[p] - S)/R[p][i]
    X[i] = round(X[i], 5)

  X1 = []
  for i in range(len(X)):
    X1.append([])
    X1[i].append(round(X[i], 5))

  return ( L1, R1, X1 )

a1 = [[4, 5, 8, 16, 33], [8, 4, 6, 10, 28], [6, 8, 2, 4, 20], [8, 6, 2, 12, 28]] # должны получаться 1
a2 = [[3, 5, 8], [2, 2, 4]] # должны получаться 1
a3 = [[3, 5, 8, 16], [2, 2, 4, 8], [1, 3, 3, 7]] # должны получаться 1
a4 = [[-3, 5, 8, 3, 3, 19], [2, 2, 4, -1, 2, 10], [1, 3, 3, -4, 8, 15], [-1, 4, 5, 6, 3, 18], [6, -6, 7, 3, 7, 23]] # не должны получаться 1
a5 = [[1,2,3],[4,5,9]]
# print(factorV1(a5))
# print(factorV2(a5))
# factorV3(a1)
# factorV4(a2)
# factorV5(a1)
# factorV6(a1)
# print(factorV7(a5))
print(factorV8(a5))
