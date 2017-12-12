import csv

x = -2
loop = 1000
alpha = 0.9

def loss(x):
    return x**2 - 4.25*x
    
def gradient(x):
    return 2*x-4.25
    
fp = open('begin.csv', 'w')
write = csv.writer(fp, delimiter=',')

for i in range(loop):
    x = x - alpha*gradient(x)
    write.writerows([[x, loss(x)]])
print(x)