
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
´´´
Conversión explícita: Es realizada expresamente por nosotros, como por ejemplo convertir de str a int con str().
```python
a = 3.5  
print(type(a)) # <class 'float'>  
a = str(a)  
print(type(a)) # <class 'str'>
´´´
## List

## Tuple

## Dictionary

# Tomando decisiones

## Sentencia if

## Ciclo For

## Ciclo While

## Break

## Continue
