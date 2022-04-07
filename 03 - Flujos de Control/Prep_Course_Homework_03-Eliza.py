## Flujos de Control

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
from cgi import print_arguments
from math import factorial


a=0
if a>0:
    print("Es mayor a 0")
elif a<0:
    print("Es menor a 0")
else:
    print("Es igual a 0")

#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
a='Elizabeth'
b=45
if(type(a)==type(b)):
    print(" son del mismo tipo")
else:
    print("no son del mismo tipo")

#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for n in range (1,21):
    if n%2==0:
        print(n,"es par")
    else:
        print(n,"no es par")

#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for n in range (0,6):
    p=n**3
    print(str(p)+"potencia")
#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
a=12
for i in range (0,a):
    print(i)
    pass

#6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, 
#sólo si la variable contiene un número entero mayor a 0
print("hola")
n=5
if type(n)==int:
    if n>0:
        factorial=n
        while n>2:
            n=n-1
            factorial=factorial*n
        print("el factorial es: ",factorial)
    else:
     print("no es mayor a 0")
else:
    print("no es un numero entero")

#7) Crear un ciclo for dentro de un ciclo while
n=0
while n<5:
    n=n+1
    for i in range (1,n):
        print("hola", n)
        print("chau chau", i)

#8) Crear un ciclo while dentro de un ciclo for

n = 5
for i in range(1, n):
    while(n < 5):
        n -= 1 #4
        print('Ciclo while nro ' + str(n))#4
        print('Ciclo for nro ' + str(i))#1
#9) Imprimir los números primos existentes entre 0 y 30
for nro in range(0, 31):
    es_primo=True
    for i in range(2, nro): 
        if (nro%i==0):
            es_primo=False
    if (es_primo):
        print(nro, "es primo")
    else:
        print(nro, 'no es primo')  

#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias
# break y/ó continue para tal fin
cantidad_ciclos = 0
for nro in range(0, 31):
    es_primo=True
    for i in range(2, nro): 
        cantidad_ciclos +=1
        if (nro%i==0):
            es_primo=False
            break
    if (es_primo):
        print(nro, "es primo")
    else:
        print(nro, 'no es primo')  
print('Cantidad de ciclos: ' +str(cantidad_ciclos))

#11) En los puntos 9 y 10, se diseño un código que encuentra números primos
# y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
ciclos_sin_break = 0
for nro in range(0, 31):
    es_primo=True
    for i in range(2, nro): 
        ciclos_sin_break +=1
        if (nro%i==0):
            es_primo=False
    if (es_primo):
        print(nro, "es primo")
    else:
        print(nro, 'no es primo')  
print('Cantidad de ciclos sin break: ' +str(ciclos_sin_break))

ciclos_con_break = 0
for nro in range(0, 31):
    es_primo=True
    for i in range(2, nro): 
        ciclos_con_break +=1
        if (nro%i==0):
            es_primo=False
            break
    if (es_primo):
        print(nro, "es primo")
    else:
        print(nro, 'no es primo')  
print('Cantidad de ciclos: ' +str(ciclos_con_break))
print('Se optimizo a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')

#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
print("Con 31: 0.3325% de optimizacion/n")
print("Con 100: 1132/4756 0.23916% de optimizacion/n")

#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12,
#  dentro del rango de números de 100 a 300

n=99
while (n<=300):
    n+=1
    if (n % 12 != 0):
        continue
    print(str(n), "es divisible por 12")

#14) Utilizar la función **input()** que permite hacer ingresos por teclado, 
# para encontrar números primos y dar la opción al usario de buscar el siguiente"
n = 1
sigue = 1
primo = True
while (sigue == 1):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
        print('¿Desea encontrar el siguiente número primo?')
        if (input() != '1'):
            print('Se finaliza el proceso')
            break
    else:
        primo = True
    n += 1



#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
n = 100
while(n<=300):
    if (n % 6 == 0):
        print('El número es: ', str(n))
        break
    n += 1

