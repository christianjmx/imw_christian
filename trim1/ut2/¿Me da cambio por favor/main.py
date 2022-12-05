import sys

dinero = int(sys.argv[1])

r = dinero//50

if r > 0:
    print("cantidad de billetes de 50€ = " +str(r))
    
resto1= dinero%50
    
e = resto1//20

if e > 0:
    print("cantidad de billetes de 20€ = " +str(e))
    
resto2= dinero%20
    
f = resto2//10

if f > 0:
    print("cantidad de billetes de 10€ = " +str(f))
    
resto3= dinero%10
    
g = resto3//5

if g > 0:
    print("cantidad de billetes de 5€ = " +str(g))

resto4= dinero%5

k = resto4//2

if k > 0:
    print("cantidad de monedas de 2€ = " +str(k))
    
resto5= dinero%2

j = resto5//1

if j > 0:
    print("cantidad de monedas de 1€ = " +str(j))