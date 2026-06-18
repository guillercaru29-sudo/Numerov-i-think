import numpy as np
import matplotlib.pyplot as plt
#Método d Numerov
#Usado para resolver y''=-g(x)y(x) + s(x)

#Oscilador Armónico con Numerov

#Pero antes, algo sencillito
# y''= -y(x)   -> g(x)=1, s(x)=0
#Sabemos que y=y0cos(x)
#Condiciones iniciales

x0=0
y0=1
dy0=0
xn=10
h=0.1
#Entonces: y=(x**2)/2
n=round((xn-x0)/h)

x=np.linspace(x0,xn,n+1)
y=np.zeros(n+1)
g=np.zeros(n+1)
s=np.zeros(n+1)
y[0]=y0
y[1]=np.cos(x[1])

def S(x):
  return 0
def G(x):
  return 1
for i in range(n+1):
  s[i]=S(x[i])
for i in range(n+1):
  g[i]=G(x[i])

for i in range(n-1):
  y[i+2]=((2*y[i+1]*(1-((5*h**2)/12)*g[i+1])) - (y[i]*(1+((h**2)/12)*g[i])) + (((h**2)/12)*(s[i+2]+10*s[i+1]+s[i])) )/(1+((h**2)/12)*g[i+2]) 
  
plt.plot(x,y, color='red')
#plt.show()
plt.plot(x,np.cos(x), color='blue')
plt.show()
print(f'Valor de las función para el último valor del dominio de x: {x[n]}')
print(f'Valor analítico y= {np.cos(x[n])}')
print(f'Valor con Numerov y= {y[n]}')
