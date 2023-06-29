import math

#Functions
dy = lambda t, y : 0.01 * y
f = lambda t : 100*math.exp(0.01*t)

#Init
ti = 0; tf = 365; step = 1
iterations = int((tf - ti) / step)
t = 0; y = 100

#Visualize
print('t   \t\t y  \t\t f(t)'); print ('%f \t %f \t %f'% (t, y, f(t)))

for i in range(1, iterations+1):
    #Euler's Method
    k1 = dy(t, y)
    #Calculate new y
    y = round(y + k1 * step, 3)
    # Update step
    t = round(t + step, 5)
    print('%f \t %f \t %f'% (t, y, f(t)))
