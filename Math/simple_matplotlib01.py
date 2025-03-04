from matplotlib import pyplot as plt
import math

def f(x):
	return math.sin(x*x)*math.cos(x)

xmin = -15
xmax = 16
xstep = 0.1

xmin_int=int(xmin // xstep)
xmax_int=int(xmax // xstep)

if int(xstep) == xstep:
	xstep_int = int(xstep)
elif xstep < 1: 
	xstep_int=int(1/xstep)
else: 
	xstep_int = int(xstep)

xrange_int = [i for i in range(xmin_int, xmax_int)]
xrange = [i*xstep for i in xrange_int]


x = [i for i in xrange]
y = [f(i) for i in x]

#plt.plot(x, y, color='green', marker = 'o', linestyle = 'solid')
plt.plot(x,y,'g-')

plt.show()

