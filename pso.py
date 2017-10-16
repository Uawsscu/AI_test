import random
import sys
import math
import csv

import matplotlib.pyplot as plt

k = 20
w = 0.5
c1 = 1.0
c2 = 1.0
loop = 10

X = []
V = []
Pbest = []
Gbest = [sys.maxint, [1, 1]]

def peaks(x, y):
    #return 3.0*pow(1.0-x,2)*math.exp(-pow(x,2)-pow(y+1.0,2)) - \
    #        10.0*(x/5.0-pow(x,3)-pow(y,5))*math.exp(-pow(x,2)-pow(y,2)) - \
    #        1.0/3.0*math.exp(-pow(x+1.0,2)-pow(y,2))
    return x*x + y*y
    
def rand(x, y):
    if x > y:
        temp = x
        x = y
        y = temp
        
    return random.uniform(x, y)

def cratePaticle():
    global Gbest

    for i in range(k):
        X.append([rand(-10, 10), rand(-10, 10)])
        V.append([rand(-10, 10), rand(-10, 10)])
        Pbest.append([sys.maxint, [X[i][0], X[i][0]]])
        
        if Pbest[i][0] <= Gbest[0]:
            Gbest[0] = Pbest[i][0]
            Gbest[1] = [X[i][0], X[i][1]]
    
            
fp = open('pso1.csv', 'w')
write = csv.writer(fp, delimiter=',')

cratePaticle()

x_axis = []
y_axis = []
print len(X)
for a in X:
    x_axis.append(a[0])
    y_axis.append(a[1])
        
plt.plot(x_axis, y_axis, 'bx')
plt.axis([-10, 10, -10, 10])
plt.show()

for i in range(loop):
    for j in range(k):
          
        r1 = rand(0, 1)
        r2 = rand(0, 1)
        
        ############################
        #temp1 = w
        #if (Gbest[1][0] < -1) and (Gbest[1][1] > 0 ):
        #    w = 0.01
        ############################    
        V[j][0] = w*V[j][0] + c1*r1*(Pbest[j][1][0]-X[j][0]) + c2*r2*(Gbest[1][0]-X[j][0])
        
        r1 = rand(0, 1)
        r2 = rand(0, 1)
        V[j][1] = w*V[j][1] + c1*r1*(Pbest[j][1][1]-X[j][1]) + c2*r2*(Gbest[1][1]-X[j][1])
        
        ############################
        #w = temp1
        ############################
       
        
        X[j][0] =  X[j][0] +  V[j][0]
        X[j][1] =  X[j][1] +  V[j][1]
        
        fitness = peaks(X[j][0], X[j][1])
        
        if fitness <= Pbest[j][0]:
            Pbest[j][0] = fitness
            Pbest[j][1] = [X[j][0], X[j][1]]
            if Pbest[j][0] <= Gbest[0]:
                Gbest[0] = Pbest[j][0]
                Gbest[1] = [X[j][0], X[j][1]]

print Gbest
    
x_axis = []
y_axis = []
print len(X)
for a in X:
    x_axis.append(a[0])
    y_axis.append(a[1])
        
plt.plot(x_axis, y_axis, 'bx')
plt.axis([-2, 2, -2, 2])
plt.show()