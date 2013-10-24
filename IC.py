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


#simple script que cifra/descifra un texto con un cifrado vernam, con la aplicacion xor.
#se le puede pasar la clave que se crea oportuna
def crypt(text, key):
    new_text = ""
    for i, c in enumerate(text):
        code = ord(c)
        xor = code ^ ord(key[i])
        new_text += chr(xor)
    return new_text

#genera una clave aleatoria en base al tamaño del texto
def get_randomkey(text):
    start = '1'
    end = '9'
    for i in range(0, len(text) - 1):
        start += '0'
        end += '9'
    key = random.randint(int(start), int(end))
    return str(key)

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
    fichero10 = open("count.txt","w")
    fichero11 = open("count2.txt","w")

    #Leemos del Fichero
    textStr = fichero.read() + fichero2.read() + fichero3.read() + fichero4.read() + fichero5.read() + fichero6.read() + fichero7.read() + fichero8.read() + fichero9.read() 

    # Primero limpiamos el texto de los caracteres peculiares
    textStr = eraseWhiteSpace(textStr)
    # Segundo quitamos los espacios
    textStr = cleanText(textStr)

    #Tercera contamos la frecuencia de las letras y hacemos sort sobre ellas
    a = countLetterFrecuency(textStr, fichero10)
    #Imprimimos el indice de coincidencia
    print(a)    
    print(indiceCoincidena(textStr, a))
    
    keygen = get_randomkey(textStr)
    print("la clave es:",keygen)
    
    textStr = crypt(textStr, keygen)
    print("Texto cifrado", textStr)
    
    a = countLetterFrecuency(textStr, fichero11)
    print(a)
    print(indiceCoincidena(textStr, a))

