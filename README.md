
# Qué es Python? ✍
Es un lenguaje de programación interpretado en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma que posee una licencia de código abierto, Python se clasifica constantemente como uno de los lenguajes de programación más populares.
# Qué es una variable? 📋
Es para indicarle al programa a partir de qué lugar empieza a existir, qué nombre tendrá y qué tipo de datos almacenará, es un elemento que se emplea para almacenar y hacer referencia a otro valor o para explicarlo de una manera más sencilla. 
## Nombrando una variable 🧾
cuando nombremos una variable hay que seguir sus reglas básicas como que no puede empezar por números y debe estar en minúscula. Al ubicar más palabras para nombrar una variable tendremos que separarlas con un guión bajo y debe tener un máximo de 15 caracteres.
```python
 variable_num  = 
 ```

## Asignando valores a una variable
Se puede asignar diferentes valores sean números o palabras.
```python
variable_num  = 12
variable_num  = [GALLETAS, TORTAS] 
```
## Operadores básicos 📝
```python
suma: +  
resta: -  
multiplicación: *  
división: /  
división entera: //  
módulo: %  
potenciación: **
```
### Suma
```python
#creamos dos variables para poder realizar la operación de la suma 
a = 12 
b = 23
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador suma  
result = (a + b)  
result = 35 
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
### Resta
```python
#creamos dos variables para poder realizar la operación  
a = 12
b = 7 
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador resta  
result = (a - b)  
result = 5  
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
### Multiplicación
```python
#creamos dos variables para poder realizar la operación  
a = 17 
b = 8 
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador de multiplicación  
result = (a * b)  
result = 136   
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
### División
```python
#creamos dos variables para poder realizar la operación  
a = 20  
b = 4  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador de división  
result = (a / b)  
result = 5  
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
### Módulo
```python
#creamos dos variables para poder realizar la operación  
a = 20  
b = 3  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador de módulo  
result = (a % b)  
result = 20  
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
# Tipos de datos en Python

## Integer
Los números enteros son aquellos que no contienen decimales, pueden ser positivos o negativos además del cero. se los conoce como de tipo int (interger, entero) o tipo long (de largo). La diferencia entre ambos es que el long permite almacenar números más grandes.

```python
x = 12 
y = 18349 
z = - 34
```
## Float 
Se utiliza para representar números decimales float (flotante) , pueden ser positivos o negativos.
```python
x = 3.09  
y = 12.0  
z = -40.25
```
## String
 Las cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. Estas cadenas de texto son de tipo str y se delimitan mediante el uso de comillas simples o dobles.
 ```python
 print("Hola bienvenido")

 ```
## Casting en Python
un cast o casting significa convertir un tipo de dato a otro, tipos de datos como los int, string o float.
Existen dos:

Conversión implícita: Es realizada automáticamente por Python. Sucede cuando realizamos ciertas operaciónes con dos tipos distintos.

```python
a = 5   # <class 'int'>  
b = 1.3 # <class 'float'>  
a = a + b  
print(a)       # 6.3
print(type(a)) # <class 'float'>
```

Conversión explícita: Es realizada expresamente por nosotros, como por ejemplo convertir de str a int con str().

```python
a = 3.5  
print(type(a)) # <class 'float'>  
a = str(a)  
print(type(a)) # <class 'str'>
```
## List
Las listas en Python son un tipo de dato que permite almacenar datos de cualquier tipo. Son mutables y dinámicas, lo cual es la principal diferencia con los sets y las tuplas, una lista sea crea con [ ] separando sus elementos con comas " , "
```python
lista = list("123456789b")                
print(lista)                              #['1', '2', '3', '4', '5', '6', '7', '8', '9', 'b']
```
## Tuple
Las tuplas se utilizan para almacenar varios elementos en una sola variable. Es una colección ordenada e inmutable significa que no pueden ser modificadas una vez declaradas, y en vez de inicializarse con corchetes se hace con ( ). 
```python
tupla = (12, 2003, 2022)
print(tupla)                     #(12, 2003, 2022)
```
## Dictionary
Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.
Un diccionario es una colección ordenada*, modificable y que no admite duplicados.
Todos los elementos en el diccionario se encuentran encerrados en un par de corchetes { }.
```python
thisdict = {  
  "brand": "TOYOTA",  
  "model": "Hilux",  
  "year": 2019  
}
print(thisdict)

[salida]: [TOYOTA Hilux 2019]
```
# Tomando decisiones📂

## Sentencia if
"if" permite que un programa ejecute unas instrucciones cuando se cumplan una condición. La estructura de control if, else, permite que un programa ejecute unas instrucciones cuando se cumple una condición y otras instrucciones cuando no se cumple esa condición. En inglés "if" significa "si" (condición) y "else" significa "si no". 
```python
#Calcular el mayor de dos números enteros introducidos por el teclado
#Entrada
num1= int(input('Ingreso num 1:'))
num2= int(input('Ingreso num 2:'))

#Proceso
if num1 > num2:
    #Salida
    print('El numero mayor es:',num1)
elif num2> num1:
    #Salida
    print('El numero mayor es:',num2)
else:
    #Salida
    print('Los números son iguales')
```
## Ciclo For
El bucle for se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario, …) y ejecutar un bloque de código. En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, sobre el cuál se pueden aplicar una serie de operaciones. 
```python
países  = [Peru, Ecuador, Argentina , Colombia]
for g in países :
    print(g)
#Su print se verá así:
#Peru 
#Ecuador
#Argentina
#Colombia
```
## Ciclo While
El uso del while nos permite ejecutar una sección de código repetidas veces, de ahí su nombre. El código se ejecutará mientras una condición determinada se cumpla. Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal.
```python
#Cuando se deje de cumplir la orden, se saldrá del bucle
x = 0
while x < 5:
    x +=1
    print(x)
#Su print se verá así:
#1
#2
#3
#4
#5
```
## Break
break permite terminar con la ejecución del bucle. Esto significa que una vez se encuentra la palabra break, el bucle se habrá terminado. 
```python
#Cuando se encuentre con el número 3, el programa terminará
x = 0
while x < 5:
    x +=1
    if x==3:
        print("Se encontró el 3")
        break
    print(x)
#Su print se verá así:
# 1
# 2
# Se encontró el 3
```
## Continue
El continue se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar. Es que el continue no rompe el bucle, si no que pasa a la siguiente iteración saltando el código pendiente. 
```python
#Cuando se encuentre con el número 3, se saltará y continuará con los demás print
x = 0
while x < 5:
    x +=1
    if x==3:
        continue
    print(x)
#Su print se verá así:
# 1
# 2
# 4
# 5
```
