import math
# import matplotlib.pyplot as plt

#Functions
dy = lambda t, y : 0.01 * y
f = lambda t : 100*math.exp(0.01*t)

#Init
ti = 0; tf = 365; step = 1
iterations = int((tf - ti) / step)
t = 0; y = 100

#Visualize
print('t   \t\t y  \t\t f(t)'); print ('%f \t %f \t %f'% (t, y, f(t)))
t_plot = []; y_RK4 = []; y_analytical = []

#RK4 Method
for i in range(1, iterations+1):
    t_plot.append(t); y_RK4.append(y); y_analytical.append(f(t))
    #Euler's Method
    k1 = dy(t, y)
    k2 = dy(t+step/2, y + k1 * step/2)
    k3 = dy(t+step/2, y + k2 * step/2)
    k4 = dy(t+step, y + k3 * step)
    #Calculate new y
    y = round(y + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4) * step, 3)
    # Update step
    t = round(t + step, 2)
    print('%f \t %f \t %f'% (t, y, f(t)))

#Plot
# t_plot.append(t); y_RK4.append(y); y_analytical.append(f(t))
# plt.plot(t_plot,y_RK4,'ro',t_plot,y_analytical)
# plt.xlabel('t'); plt.ylabel('y')
# plt.legend(["Runge-Kutta", "Actual"])
# plt.show()