# GENERADORES

Las funciones generadoras son un tipo especial de funciones que devuelven un generador ("lazy iterator"), que son objetos iterables pero, al contrario que otros iterables como las listas, no almacenan sus elementos en memoria y sólo se puede iterar sobre ellos una vez.

Son especialmente útiles cuando hay que utilizar grandes cantidades de valores, que de otro modo ocuparían mucha memoria.

Utilizan el término _yield_ en lugar de _return_.

Ejemplo:

Para generar una secuencia de números infinita se necesita utilizar un generador, ya que la memoria de nuestro ordenador es finita.

```
def infinite():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite():
    print(i)
```

El resultado de ejecutar este código es el siguiente:

```
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
KeyboardInterrupt: Forced reset
```

El programa se continúa ejecutando hasta que se para manualmente.

En lugar de usar un bucle for, se puede usar el método next() sobre el objeto generador para comprobar que los generadores devuelven lo que esperamos:

```
gen = infinite()
print(next(gen))
print(next(gen))
print(next(gen))
```

Resultado:

```
0
1
2
```

Se puede asignar el generador a una variable. Cuando se llaman un método sobre el generador, como por ejemplo next(), se ejecuta el código de la función hasta el _yield_. Cuando llega al _yield_, el programa suspende la ejecución de la función y devuelve el valor creado. Cuando una función finaliza, su estado se conserva.

Otro ejemplo de una función generadora que devuelve una lista de números en un rango determinado:

```
def make_range(n):
    i = 0
    while i < n:
        yield i
        i +=1

range = make_range(5)
print(range)
print(list(range))
```

Resultado:

```
<generator object make_range at 0x7fe266875ca8>
[0, 1, 2, 3, 4]
```

Esta función sería similar a esta:

```
def make_range(n):
    to_return = []
    i = 0
    while i < n:
        to_return += [i]
        i += 1
    return to_return
```

Resultado:

```
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
```
