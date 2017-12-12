import numpy as np
import csv

def gradient(X, y, theta):
    m = len(X)
    theta_grad = np.array([0, 0])
    for i in range(m):
        theta_grad[0] += (2.0/(m))*((theta[0] + theta[1]*X[i]) - y[i])
        theta_grad[1] += (2.0/(m))*((theta[0] + theta[1]*X[i]) - y[i])*X[i]
    return theta_grad

def loss(X, y, theta):
    m = len(X)
    J = 0
    for i in range(m):
        J += (1./(2*m))*((theta[0] + theta[1]*X[i]) - y[i])**2
    return J

fp = open('begin.csv', 'w')
write = csv.writer(fp, delimiter=',')

data = np.genfromtxt("data.csv", delimiter=",") # read csv file (don't forget to download!)
#print(data[:,0])
X = data[:,0]
y = data[:,1]
J = [] # history of cost
theta = np.array([0, -1]) # intial theta
n_iter = 300
for i in range(n_iter):
    write.writerows([[theta[0], theta[1]]])
    theta_grad = gradient(X, y, theta)
    theta = theta - 0.0001*theta_grad
    J.append(loss(X, y, theta))
    
    #print()
print ('final theta = %s' % theta)
print ('final cost = %s' % J[-1])