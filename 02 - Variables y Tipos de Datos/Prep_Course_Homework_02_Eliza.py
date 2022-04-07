## Variables

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

bebecita=24
print(bebecita)
#2) Imprimir el tipo de dato de la constante 8.5
print(type(8.5))

#3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(bebecita))

#4) Crear una variable que contenga tu nombre
nombre='Elizabeth'
print(nombre)
#5) Crear una variable que contenga un número complejo
n_complejo=1-2j
print(n_complejo)
#6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(n_complejo))
#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
import math
v_pi=math.pi
print(v_pi)
num_pi=round(v_pi,4)
print(num_pi)
#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
v_t='True'
v_tt=True
print(v_t)
print(v_tt)
#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(v_t))
#10) Asignar a una variable, la suma de un número entero y otro decimal
n1=14
n2=15.45
suma=n1+n2
print(suma)
#11) Realizar una operación de suma de números complejos
n_c=1+14j
n1_c=2+15j
s_complejo=n_c+n1_c
print(s_complejo)
#12) Realizar una operación de suma de un número real y otro complejo
n_r=12.3
print(n_r + n_c)

#13) Realizar una operación de multiplicación
a=3
m=6
print(a*m)

#14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
dividendo=27
divisor=4
cociente=27/4
print(cociente)

#16) De la división anterior solamente mostrar la parte entera

cociente=27//4
print(cociente)
#17) De la división de 27 entre 4 mostrar solamente el resto
resto=27%4
print(resto)
#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
dividendo=resto+divisor*cociente
print(dividendo)

#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
word1='Hola soy'
word2=' Elizabeth'
word3=word1+word2
print(word3)
#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print("pon")
print(2=='2')
#21)( Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(type(2==int('2')))
#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
print( "PregunTa #22 porque no se puede convertir de string a float")
#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
a = -3
a -= 1
print(a)
#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print("1<<2")
print(1<<2)
print("es un sistema de numeración en el que los números se representan utilizando las cifras 0 y 1")
#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
float(2) + float('2')

#26) Realizar una operación válida entre valores de tipo entero y string
var1 = 'este texto se repite '
var2 = 3
print(var1 * var2 + str(var2) + ' veces' )