#!/usr/bin/env python3
# coding: utf8
# Author: Jose Miguel Colella


import random
# Importo esto para ordenar el diccionario de frecuencias
# que no esta ordenado
import collections

# Constante que contiene las minusculas
# Hay 27 caracteres en el alfabeto
#ALPHABET_LOWERCASE = string.ascii_lowercase + "ñ"
lista_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "ñ", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                "x", "y", "z"]


def cleanText(text):
    """
    Función creada para reemplazar los caracteres peculiares
    del lenguaje castellano
    """
    text = text.replace("á", "a")
    text = text.replace("é", "e")
    text = text.replace("í", "i")
    text = text.replace("ó", "o")
    text = text.replace("ú", "u")
    text = text.replace("ü", "u")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace(";", "")
    text = text.replace(":", "")
    text = text.replace("!", "")
    text = text.replace("¡", "")
    text = text.replace("?", "")
    text = text.replace("¿", "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace("/", "")
    text = text.replace("'", "")
    text = text.replace("-", "")
    text = text.replace("*", "")
    text = text.replace("\n", "")
    # Todo el texto a minuscula
    text = text.lower()
    return text


def eraseWhiteSpace(text):
    """
    Función que elimina los espacios en blanco
    """
    # Con esto quitamos los espacios
    text = ''.join(text.split())
    return text


def countLetterFrecuency(text, textout):
    # Al final devuelve el diccionario de frecuencia ordenado
    freqDict = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
        "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
        "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0,
        "x": 0, "y": 0, "z": 0, "ñ": 0}
    # Para contar la frecuencia de las letras usamos lo siguiente
    for i in lista_letras:
        a = i + ": " + str(text.count(i))
        freqDict[i] = text.count(i)
        textout.write(a)
        textout.write("\n")
    return collections.OrderedDict(sorted(freqDict.items(),
                                   key=lambda t: t[0]))


def indiceCoincidena(text, dictFreq):
    """El indice de coincidencia se la
    (fa(fa-1)*fb(fb-1)+...+fz(fz-1))/n(n-1)
    Esto significa la frecuencia de las todas las lista
    en la cual en cada una se multiplica por la frecuencia menos
    1 dividido por n que es la longitud del texto por el numero
    menos 1
    El indice de coincidencia esta cerca de lo normal
    """
    # Primero calculamos el numero de caracteres
    numTotalesChar = len(text)
    freqTot = 0
    for i in lista_letras:
        if i in dictFreq:
            freqTot += dictFreq[i] * (dictFreq[i] - 1)
    ic = freqTot / (numTotalesChar * (numTotalesChar - 1))

    return ic


def permutacion(text):
    # aplica la permutacion a un texto y crea uno nuevo
    # la permutacion es una aleatoria entre los caracteres de ascii en
    # minuscula
    i = random.randint(0, 27)
    for j in range(27):
        text.replace(lista_letras[j], lista_letras[i])
        i = i + 1
        i = i % 27


if __name__ == '__main__':
    fichero = open("test.txt")
    fichero2 = open("process.txt", "w")
    fichero3 = open("count.txt", "w")
    fichero4 = open("permutacion.txt", "w")

    #Leemos del Fichero
    textStr = fichero.read()

    # Primero limpiamos el texto de los caracteres peculiares
    textStr = eraseWhiteSpace(textStr)
    # Segundo quitamos los espacios
    textStr = cleanText(textStr)

    #Tercera contamos la frecuencia de las letras y hacemos sort sobre ellas
    a = countLetterFrecuency(textStr, fichero3)

    #Imprimimos el indice de coincidencia
    print(indiceCoincidena(textStr, a))

    #TODAVIA QUEDA DEFINIR LAS PERMUTACIONES Y CALCULAR EL IC DE ELLAS
