import math
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(1500)

# dy/dx = y, 0<x<=1, y(0) = 1
# solution is obviously y = exp(x)
# discretisation of interval [0,1]
# Integer N > 0 - number of grid points
# xk = k*h, where h = 1/N, k = 0,1...N, x0 = 0
y0 = 1
y1 = math.exp(1)

def y_helper(n, N):
    if n == 0:
        return 1.0
    else:
        h = 1.0 / N
        return (1 + h) * y_helper(n-1, N)
# calculates yN
def y(n):
    return y_helper(n,n)


#---------------- Calculates approximations and errors ------------
approximation = []
error = []
hlist = []
for i in range(1,11):
    approximation.append(y(2**i))
    error.append(math.log(abs(y(2**i) - y1)))
    hlist.append(math.log(1.0/i))

#---------------- Prints approximations and errors -------------------
print "Approximations:"
for i in range(len(approximation)):
    print approximation[i]

print "log(error):"
for i in range(len(error)):
    print error[i]

print "log(h):"
for i in range(len(hlist)):
    print hlist[i]



#------------------------------ Plotting --------------------------
plt.xlim(0,9)
plt.plot(error, label='log(error)')
plt.plot(hlist, label='log(h)')
plt.legend()
plt.show()
