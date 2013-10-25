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
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                "x", "y", "z"]


def cleanText(text):
    """
    Función creada para reemplazar los caracteres peculiares
    del lenguaje castellano
    """

    text = text.replace("\xe1", "a")
    text = text.replace("\xe9", "e")
    text = text.replace("\xed", "i")
    text = text.replace("\xf3", "o")
    text = text.replace("\xf3", "u")
    text = text.replace("ü", "u")
    text = text.replace("\xf1", "n")
    text = text.replace("\xfa", "")
    text = text.replace("\xd1", "")
    text = text.replace(".", "")
    text = text.replace(",", "")
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
    text = text.replace(":", "")
    text = text.replace("\xda", "")
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace(";", "")
    text = text.replace("\xa1", "")
    text = text.replace("\xcd", "")
    text = text.replace("\xef", "")
    text = text.replace("\xfc", "")
    text = text.replace("\xbf", "")
    text = text.replace("\xfc", "")
    text = text.replace("\xc9", "")
    text = text.replace("&", "")
    text = text.replace("\xfc", "")
    text = text.replace("\xfc", "")
    text = text.replace("1", "")
    text = text.replace("2", "")
    text = text.replace("3", "")
    text = text.replace("4", "")
    text = text.replace("5", "")
    text = text.replace("6", "")
    text = text.replace("7", "")
    text = text.replace("8", "")
    text = text.replace("9", "")
    text = text.replace("0", "")
    text = text.replace("\xba", "")
    text = text.replace("\xfc", "")
    text = text.replace("\xfc", "")
    text = text.replace("\xfc", "")
    text = text.replace("\xfc", "")

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
    for i in dictFreq.keys():
        freqTot += float(dictFreq[i] * (dictFreq[i] - 1))
    ic = float(freqTot / (numTotalesChar * (numTotalesChar - 1)))

    return ic


def codificar(text, numPermutaciones):
    textOut = ""
    listOfCipherAl = []
    for i in range(numPermutaciones):
        listaCipher = lista_letras[:]
        random.shuffle(listaCipher)
        listOfCipherAl.append(listaCipher)
    count = 0
    for x in range(len(text)):
        textOut += listOfCipherAl[count][listaCipher.index(text[x])]
        count += 1
        count = count % numPermutaciones

    return textOut

if __name__ == '__main__':
    fichero = open("calderon1.txt")
    procesado = open("process.txt", "w")
    permutado = open("permutado.txt", "w")
    fichero10 = open("count.txt", "w")
    fichero11 = open("count2.txt", "w")
    cad = ""

    # Leemos del Fichero
    textStr = fichero.read()

    # Primero limpiamos el texto de los caracteres peculiares
    textStr = eraseWhiteSpace(textStr)
    # Segundo quitamos los espacios
    textStr = cleanText(textStr)
    procesado.write(textStr)
    procesado.close()

    # Tercera contamos la frecuencia de las letras y hacemos sort sobre ellas
    a = countLetterFrecuency(textStr, fichero10)
    # Imprimimos el indice de coincidencia
    # print(a)
    print(indiceCoincidena(textStr, a))

    textStr = codificar(textStr, 20)
    permutado.write(textStr)
    a = countLetterFrecuency(textStr, fichero11)
    # print(a)
    print(indiceCoincidena(textStr, a))
