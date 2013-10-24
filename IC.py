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
                "m", "n", "ñ" , "o", "p", "q", "r", "s", "t", "u", "v", "w",
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
    text = text.replace("ñ", "n")
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


def countLetterFrecuency(text,textout):
    # Al final devuelve el diccionario de frecuencia ordenado
    freqDict = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
        "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
        "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0,
        "x": 0, "y": 0, "z": 0, "ñ":0}
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
        freqTot += dictFreq[i] * (dictFreq[i] - 1)
    ic = freqTot / (numTotalesChar * (numTotalesChar - 1))

    return ic

def init(b):    
    global cad
    global dic
    global dic2     
    dic = {"a": b[0:3], "b": b[3:6], "c": b[6:9] , "d": b[9:12] , "e": b[12:15], 
    "f": b[15:18], "g": b[18:21], "h": b[21:24], "i": b[24:27], "j": b[27:30],
    "k": b[30:33], "l": b[33:36], "m": b[36:39], "n": b[39:42], "o": b[42:45],
    "p": b[45:48], "q": b[48:51], "r": b[51:54], "s": b[54:57], "t": b[57:60],
    "u": b[60:63], "v": b[63:66], "w": b[66:69], "x": b[69:72], "y": b[72:75],
    "z": b[75:78], " ": b[78:81]}

    dic2 = {b[0:3]: "a", b[3:6]: "b", b[6:9]: "c", b[9:12]: "d", b[12:15]: "e", 
    b[15:18]: "f", b[18:21]: "g", b[21:24]: "h", b[24:27]: "i", b[27:30]: "j", 
    b[30:33]: "k", b[33:36]: "l", b[36:39]: "m", b[39:42]: "n", b[42:45]: "o", 
    b[45:48]: "p", b[48:51]: "q", b[51:54]: "r", b[54:57]: "s", b[57:60]: "t", 
    b[60:63]: "u", b[63:66]: "v", b[66:69]: "w", b[69:72]: "x", b[72:75]: "y", 
    b[75:78]: "z", b[78:81]: " "}
    
    cad=b
    
def codificar(cadena):
    res=""
    for x in cadena:
        x = chr(x)
        res+=dic[x]
        res+=("*")
    print "cadena de codificacion:", cad
    return res
    
def descodificar(code):
    res="" 
    for x in code.split("*"):
        if x!="":
            x = chr(x)
            res+=dic2[x]
    print "cadena de codificacion:", cad
    return res 

def cambiar():
    res=""
    for x in cad:
        res+=char[x]
    print "cadena de codificacion cambiada a:", res
    init(res)

if __name__ == '__main__':
    fichero = open("calderon1.txt")
    fichero2 = open("carrol1.txt")
    fichero3 = open("cerv1.txt")
    fichero4 = open("darwin1.txt")
    fichero5 = open("galdos1.txt")
    fichero6 = open("galdos2.txt")
    fichero7 = open("kipling1.txt")
    fichero8 = open("lazarillo.txt")
    fichero9 = open("2donq10.txt")
    procesado = open("process.txt","w")
    fichero10 = open("count.txt","w")
    fichero11 = open("count2.txt","w")
    char = {"a": "f", "b": "g", "c": "h", "d": "i", "e": "j", "f": "k", "g": "l",
    "h":"m", "i":"n","j":"o","k": "p", "l": "q", "m": "r", "n": "s", "o": "t", "p": "u",
    "q": "v", "r": "w", "s": "x", "t": "y", "u": "z", "v": "a", "w": "b", 
    "x": "c", "y": "d", "z": "e"}
    
    cad=""

    #Leemos del Fichero
    textStr = fichero.read()

    # Primero limpiamos el texto de los caracteres peculiares
    textStr = eraseWhiteSpace(textStr)
    # Segundo quitamos los espacios
    textStr = cleanText(textStr)
    procesado.write(textStr)
    procesado.close()

    #Tercera contamos la frecuencia de las letras y hacemos sort sobre ellas
    a = countLetterFrecuency(textStr, fichero10)
    #Imprimimos el indice de coincidencia
    print(a)    
    print(indiceCoincidena(textStr, a))
    
    cambiar()

    codificar(textStr)

    descodificar(textStr)
    
    
    a = countLetterFrecuency(textStr, fichero11)
    print(a)
    print(indiceCoincidena(textStr, a))

