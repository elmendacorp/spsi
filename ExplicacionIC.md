Programa para el calculo del Indice de Coincidencia
===================================================

Autores:
Jose Miguel Colella y Francisco Ruiz Lopez
---------------------------------------------------

Para resolver el problema del calculo del IC, hemos automatizado el proceso
del calculo usando el lenguaje de programación Python.

Las funciones principales que se han creado son:

```python
def cleanText(2stext):
def eraseWhiteSpace(text):
def indiceCoincidena(text,dictFreq):
def codificar(text, numPermutaciones):
```

Primero se ha limpiado el texto, quitando los caracteres especiales, como
los que tienen tilde, la ñ y los simbolos de puntuación. Después de limpiar
el texto, se ha quitado los espacios en blanco. Cuando se ha quitado los espacios
en blanco, ya podemos calcular el indice de coincidencia, usando la siguiente formula:

```
IC = (fa(fa - 1) + fb(fb - 1) + ... + fz(fz - 1)) / n(n - 1)
-> Donde n es el número de letras del texto
```


En más detalle para el calculo del IC, se ha calculado el número de caracteres
en el texto. Recoremos las llaves del diccionario de entrada y hacemos la suma
de fx(fx - 1). Los dividimos por el número de caracteres multiplicado por el
número de caracteres menos 1.

Para codificar el text se ha creado alfabetos de cifrados en base al número
de permutaciones, creando una lista de alfabetos de cifrado. Usando dicha lista,
ciframos el texto en base al numero de permutaciones. Por ejemplo, si tenemos
dos permutaciones, se crean dos alfabetos de cifrado, que se guardan en la lista
de alfabetos de cifrado. Ahora el primer caracter se cifra con el primer alfabeto,
el segundo alfabeto, el tercer caracter con el primer alfabeto, etc...
Se devuelve el texto cifrado.









