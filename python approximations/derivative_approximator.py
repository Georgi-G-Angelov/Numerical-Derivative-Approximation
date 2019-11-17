import matplotlib.pyplot as plt
import math

# (i) f'(x) ~ (f(x+h)-f(x)) / h
# (ii) f'(x) ~ (f(x)-f(x-h)) / h
# (iii) f'(x) ~ (f(x+h)-f(x-h)) / (2h)
def approximation(f1, f2, h):
    return (f1-f2) / h

def f(x):
    return x**3

actualValue = 3
hlist = []
lists = [[],[],[]]
errors = [[],[],[]]
logErrors = [[],[],[]]
approximations = [[],[],[]]

#------------- Calculation approximations and errors --------------
for i in range(1,11):
    h = 1.0 / (2**i)
    approximations[0] = approximation(f(1+h), f(1), h)
    approximations[1] = approximation(f(1), f(1-h), h)
    approximations[2] = approximation(f(1+h), f(1-h), 2*h)
    for j in range(3):
        lists[j].append(approximations[j])
        logErrors[j].append(math.log(abs(approximations[j] - actualValue)))
        errors[j].append(abs(approximations[j] - actualValue))

    hlist.append(math.log(h))

#-------------- Printing approximations and errors --------------
for j in range(3):
    print ("approximation" + str(j+1) + ":")
    for i in range(len(lists[j])):
        print lists[j][i]

for j in range(3):
    print ("error" + str(j+1) + ":")
    for i in range(len(errors[j])):
        print errors[j][i]

for j in range(3):
    print ("log(error" + str(j+1) + "):")
    for i in range(len(logErrors[j])):
        print logErrors[j][i]

print "log(h):"
for i in range(len(hlist)):
    print hlist[i]

# ------------ Plotting ------------
plt.xlim(0,9)
#plt.plot(hlist, label='log(h)')
plt.xlabel('log(h)')
plt.ylabel('log(x)')


for i in range(3):
    plt.plot(logErrors[i], label = 'log(error'+str(i+1)+')')


plt.legend()
plt.show()
